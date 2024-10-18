from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from .models import Repository,File,Issue,Collaborator


# Create your views here.


def register()