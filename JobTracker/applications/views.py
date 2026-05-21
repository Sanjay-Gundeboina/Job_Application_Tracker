from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import JobApplication
from .serializer import JobApplicationSerializer

from openai import OpenAI
from django.conf import settings

@api_view(['GET','POST'])
def application_list(req):
    if req.method=='GET':
        status_filter=req.GET.get('status')
        applications=JobApplication.objects.all()
        if status_filter:
            applications=applications.filter(status=status_filter)        
        serializer=JobApplicationSerializer(applications,many=True)
        return Response(serializer.data)

    elif req.method=='POST':
        app_data=req.data
        serializer=JobApplicationSerializer(data=app_data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PATCH','DELETE'])
def application_detail(req,key):
    try:
        app_data=req.data
        application=JobApplication.objects.get(id=key)
        print(application)
    except Exception as e:
        return Response({"error":str(e)},status=status.HTTP_404_NOT_FOUND)
    
    if req.method=="GET":
        serializer=JobApplicationSerializer(application)
        return Response(serializer.data)
    
    elif req.method=="PATCH":
        serializer=JobApplicationSerializer(application,app_data,partial=True)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif req.method=="DELETE":
        application.delete()
        return Response({"msg":"Deleted Successfully"})
    
@api_view(['GET'])
def application_summary(req):
    applied_count=JobApplication.objects.filter(status='applied').count()
    print(applied_count)
    interviewing_count=JobApplication.objects.filter(status='interviewing').count()
    rejected_count=JobApplication.objects.filter(status='rejected').count()
    offered_count=JobApplication.objects.filter(status='offered').count()

    summary={
        "applied":applied_count,
        "interviewing":interviewing_count,
        "rejected":rejected_count,
        "offered":offered_count
    }

    return Response(summary)

@api_view(['POST'])
def generate_followup(req,key):
    try:
        application=JobApplication.objects.get(id=key)
    except Exception as e:
        print("application not found")
        return Response({"error":str(e)},status=status.HTTP_404_NOT_FOUND)
    
    prompt=f""" 
    write a consise and professional follow up email.
    company:{application.company}
    role:{application.role}
    keep  under 100 words"""

    try:
        client=OpenAI(api_key=settings.OPENAI_API_KEY)
        response=client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )

        return Response({
            "email":
            response.choices[0].message.content
        })
    
    except Exception as e:
        print(e)
        return Response({
            "error":"Unable to generate follow-up email. Please check  your open ai secret key configuration."
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
