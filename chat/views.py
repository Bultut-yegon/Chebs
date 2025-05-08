from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message, Like
from .forms import ChatForm
from django.http import JsonResponse

# Create your views here.

@login_required
def chat_view(request):
    messages = Message.objects.all()
    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            message = Message(sender=request.user, content=form.cleaned_data["content"])
            message.save()
            return redirect('chat')
    else:
        form = ChatForm()
    return render(request,'chat/chat.html',{'messages':messages,'form':form})

def like_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    like, created = Like.objects.get_or_create(user=request.user, message=message)
    if not created:
        like.delete()
        liked = False
    else:
        liked = True
    return JsonResponse({'likes': message.liked_count, 'liked':liked})
