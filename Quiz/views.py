from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date
# Create your views here.
def Home(request):
    return render(request,'index.html')
def About(request):
    return render(request,'about.html')
def Studentlogin(request):
    error = ""
    UserDetail.objects.all()
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['password']
        user1 = authenticate(username=u, password=p)
        try:
            user = User.objects.get(username=u)
            cat1 = UserDetail.objects.get(user=user)
        except:
            pass
        if user1 and cat1.cat == "student":
            login(request, user1)
            error = "no"
        else:
            error = "yes"
    d = {'error': error}
    return render(request,'studentlogin.html',d)

def Contact(request):
    return render(request,'contact.html')

def StudentDashboard(request):
    if not request.user.is_authenticated:
        return redirect('studentlogin')
    return render(request,'studentdashboard.html')

def Tutorlogin(request):
    error = ""
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['password']
        user1 = authenticate(username=u,password=p)
        try:
            user = User.objects.get(username=u)
            cat1 = UserDetail.objects.get(user=user)
        except:
            pass
        if user1 and cat1.cat == "tutor":
            login(request, user1)
            error = "no"
        else:
            error = "yes"
    d = {'error': error}
    return render(request,'tutorlogin.html',d)

def Userdashboard(request):
    if not request.user.is_authenticated:
        return redirect('tutorlogin')
    return render(request,'userdashboard.html')

def addTopic(request):
    if not request.user.is_authenticated:
        return redirect('tutorlogin')
    course = Course.objects.all()
    if request.method == "POST":
        c = request.POST['course']
        l = request.POST['level']
        r = request.POST['regular_news']
        de = request.POST['desc']
        Topic.objects.create(course=Course.objects.filter(course_name=c).first(), level=l, topic=r, description=de)
    d = {'course':course}
    return render(request,'addtopic.html',d)

def addCourse(request):
    if not request.user.is_authenticated:
        return redirect('tutorlogin')
    if request.method == "POST":
        c = request.POST['course']
        d = request.POST['desc']
        Course.objects.create(course_name=c, description=d)
    return render(request,'addcourse.html')

def addQuestion(request):
    if not request.user.is_authenticated:
        return redirect('tutorlogin')
    course1 = Course.objects.all()
    topic1 = Topic.objects.all()
    if request.method == "POST":
        t = request.POST['select_topic']
        q = request.POST['fullQuestion']
        o1 = request.POST['option1']
        o2 = request.POST['option2']
        o3 = request.POST['option3']
        o4 = request.POST['option4']
        a = request.POST['answer']
        Question.objects.create(topic=Topic.objects.filter(topic=t).first(), question=q, option1=o1, option2=o2, option3=o3, option4=o4, answer=a)
    d = {'course':course1, 'topic':topic1}
    return render(request,'addquestion.html',d)


def addUser(request):
    if not request.user.is_authenticated:
        return redirect('tutorlogin')
    if request.method == "POST":
        u = request.POST['loginid']
        cat = request.POST['select_topic']
        f = request.POST['fname']
        l = request.POST['lname']
        p1 = request.POST['password']
        p2 = request.POST['cpassword']
        g = request.POST['gender']
        e = request.POST['email']
        m = request.POST['mob']
        d = request.POST['dob']
        add1 = request.POST['address1']
        add2 = request.POST['address2']
        c = request.POST['user_city']
        s = request.POST['user_state']
        co = request.POST['user_country']
        i = request.FILES['image']

        user = User.objects.create_user(username=u, first_name=f, last_name=l, password=p1, email=e)
        UserDetail.objects.create(user=user, gender=g, mobile=m, dob=d, add1=add1, add2=add2, city=c, country=co, img=i)

    return render(request,'adduser.html')

def TutorReport(request):
    if not request.user.is_authenticated:
        return redirect('tutorlogin')
    tutor = []
    for i in UserDetail.objects.all():
        if i.cat == "tutor":
            tutor.append(i)
    d = {'userdetail': tutor}
    return render(request,'tutorreport.html',d)

def StudentReport(request):
    if not request.user.is_authenticated:
        return redirect('tutorlogin')
    student1 = UserDetail.objects.filter(cat="student")
    d = {'userdetail': student1}
    return render(request,'studentreport.html',d)


def TopicDetail(request):
    if not request.user.is_authenticated:
        return redirect('tutorlogin')
    student1 = Topic.objects.all()
    d = {'topicdetail': student1}
    return render(request,'topicreport.html',d)

def CourseReport(request):
    if not request.user.is_authenticated:
        return redirect('tutorlogin')
    student1 = Course.objects.all()
    d = {'topicdetail': student1}
    return render(request,'coursereport.html',d)


def QuestionReport(request):
    if not request.user.is_authenticated:
        return redirect('tutorlogin')
    student1 = Question.objects.all()
    d = {'topicdetail': student1}
    return render(request,'questionreport.html',d)


def MyAccount(request,pid):
    if not request.user.is_authenticated:
        return redirect('tutorlogin')
    data1 = User.objects.get(id=pid)
    data = UserDetail.objects.get(user=data1)
    if data:
        if request.method == "POST":
            u = request.POST['loginid']
            f = request.POST['fname']
            l = request.POST['lname']
            e = request.POST['email']
            m = request.POST['mob']
            add1 = request.POST['address1']
            add2 = request.POST['address2']
            c = request.POST['user_city']
            s = request.POST['user_state']
            co = request.POST['user_country']
            data.user.first_name = f
            data.user.last_name = l
            data.user.username = u
            data.user.email = e
            data.mobile = m
            data.add1 = add1
            data.add2 = add2
            data.country = co
            data.city = c
            data.state = s
            data.user.save()
            data.save()
            try:
                i = request.FILES['image']
                data.img = i
                data.save()
            except:
                pass

    d = {'data':data}

    return render(request,'myaccount.html',d)


def MyAccountStudent(request,pid):
    if not request.user.is_authenticated:
        return redirect('tutorlogin')
    data1 = User.objects.get(id=pid)
    data = UserDetail.objects.get(user=data1)
    if data:
        if request.method == "POST":
            u = request.POST['loginid']
            f = request.POST['fname']
            l = request.POST['lname']
            e = request.POST['email']
            m = request.POST['mob']
            add1 = request.POST['address1']
            add2 = request.POST['address2']
            c = request.POST['user_city']
            s = request.POST['user_state']
            co = request.POST['user_country']
            data.user.first_name = f
            data.user.last_name = l
            data.user.username = u
            data.user.email = e
            data.mobile = m
            data.add1 = add1
            data.add2 = add2
            data.country = co
            data.city = c
            data.state = s
            data.user.save()
            data.save()
            try:
                i = request.FILES['image']
                data.img = i
                data.save()
            except:
                pass

    d = {'data':data}

    return render(request,'myaccountstudent.html',d)

def ChangePassword(request,pid):
    if not request.user.is_authenticated:
        return redirect('tutorlogin')
    user = User.objects.get(id=pid)
    if request.method=="POST":
        p = request.POST['pass1']
        request.user.set_password(p)
        request.user.save()
        return redirect('tutorlogin')

    return render(request,'changepassword.html')


def ChangePassword2(request,pid):
    if not request.user.is_authenticated:
        return redirect('studentlogin')
    user = User.objects.get(id=pid)
    if request.method == "POST":
        p = request.POST['pass1']
        request.user.set_password(p)
        request.user.save()
        return redirect('studentlogin')
    return render(request,'changepassword2.html')

def MyResult(request,pid):
    if not request.user.is_authenticated:
        return redirect('studentlogin')
    user = User.objects.get(id=pid)
    user1 = UserDetail.objects.filter(user=user).first()
    data = QuizResult.objects.filter(bhu=user1)
    d = {'data':data}
    return render(request,'myresult.html',d)


def CourseList(request):
    if not request.user.is_authenticated:
        return redirect('studentlogin')
    data = Course.objects.all()
    d = {'topicdetail': data}
    return render(request,'courselist.html',d)


def ViewTopic(request,pid):
    if not request.user.is_authenticated:
        return redirect('studentlogin')
    data1 = Course.objects.get(id=pid)
    data = Topic.objects.filter(course=data1)
    d = {'topicdetail': data}
    return render(request,'viewtopic.html',d)

def StartQuiz(request,pid):
    if not request.user.is_authenticated:
        return redirect('studentlogin')
    data1 = Topic.objects.get(id=pid)
    data = Question.objects.filter(topic=data1)
    final=[]
    if request.method == "POST":
        li = []
        p = len(data)+1
        que1=""
        for i in range(1,p):
            que = "que"+str(i)
            try:
                que1=request.POST[que]
            except:
                pass
            if que1:
                li.append(que1)
            else:
                li.append("------")
        count=0
        total = 0
        for i in range(0,len(data)):
            total+=1
            if Question.objects.filter(answer=li[i]):
                count+=1

        correct = str(count)+" "+"out of"+" "+str(total)
        date2 = date.today()
        result1 = ""
        if total == count:
            result1 = "pass"
        else:
            result1 = "fail"

        user = User.objects.get(username=request.user.username)
        quiz = QuizResult.objects.create(bhu=UserDetail.objects.get(user=user), topic=data1, marks=correct,date1=date2, result=result1)
        for i in data:
            final.append(i)
        for j in range(0,len(data)):
            FinalResult.objects.create(quiz=quiz,que=final[j],your_ans=li[j])
        return redirect('viewresult',quiz.id)
    d = {'topic': data}
    return render(request,'startquiz.html',d)

def Logout(request):
    logout(request)
    return redirect('home')

def DeleteTutor(request,pid):
    if not request.user.is_authenticated:
        return redirect('tutorlogin')
    if UserDetail.objects.filter(id=pid).exists():
        data = UserDetail.objects.get(id=pid)
        data.delete()
        return redirect('tutorreport')

def DeleteStudent(request,pid):
    if not request.user.is_authenticated:
        return redirect('tutorlogin')
    if UserDetail.objects.filter(id=pid).exists():
        data = UserDetail.objects.get(id=pid)
        data.delete()
        return redirect('studentreport')

def DeleteQuestion(request,pid):
    if not request.user.is_authenticated:
        return redirect('tutorlogin')
    if Question.objects.filter(id=pid).exists():
        data = Question.objects.get(id=pid)
        data.delete()
        return redirect('questionreport')

def DeleteTopic(request,pid):
    if not request.user.is_authenticated:
        return redirect('tutorlogin')
    if Topic.objects.filter(id=pid).exists():
        data = Topic.objects.get(id=pid)
        data.delete()
        return redirect('topicreport')

def DeleteCourse(request,pid):
    if not request.user.is_authenticated:
        return redirect('tutorlogin')
    if Course.objects.filter(id=pid).exists():
        data = Course.objects.get(id=pid)
        data.delete()
        return redirect('coursereport')

def EditCourse(request,pid):
    if not request.user.is_authenticated:
        return redirect('tutorlogin')
    data = Course.objects.get(id=pid)
    if request.method == "POST":
        c = request.POST['course']
        desc = request.POST['desc']
        data.course_name = c
        data.description = desc
        data.save()
    d = {'data':data}
    return render(request, 'editcourse.html',d)

def EditTopic(request,pid):
    if not request.user.is_authenticated:
        return redirect('tutorlogin')
    data1 = Course.objects.all()
    data = Topic.objects.get(id=pid)
    error = False
    if request.method == "POST":
        l = request.POST['level']
        r = request.POST['regular_news']
        de = request.POST['desc']
        data.level = l
        data.topic = r
        data.description = de
        data.save()
        for i in Course.objects.all():
            if i.id==data.course.id:
                error = True
    d = {'data':data,'course1':data1,'error':error}

    return render(request, 'edittopic.html',d)

def EditStudent(request,pid):
    if not request.user.is_authenticated:
        return redirect('tutorlogin')
    data = UserDetail.objects.get(id=pid)
    if request.method == "POST":
        u = request.POST['loginid']
        f = request.POST['fname']
        l = request.POST['lname']
        e = request.POST['email']
        m = request.POST['mob']
        add1 = request.POST['address1']
        add2 = request.POST['address2']
        c = request.POST['user_city']
        s = request.POST['user_state']
        co = request.POST['user_country']
        data.user.first_name = f
        data.user.last_name = l
        data.user.username = u
        data.user.email = e
        data.mobile = m
        data.add1 = add1
        data.add2 = add2
        data.country = co
        data.city = c
        data.state = s
        data.user.save()
        data.save()
        try:
            i = request.FILES['image']
            data.img = i
            data.save()
        except:
            pass
    d = {'data': data}
    return render(request, 'editstudent.html',d)

def EditTutor(request,pid):
    if not request.user.is_authenticated:
        return redirect('tutorlogin')
    data = UserDetail.objects.get(id=pid)
    if request.method == "POST":
        u = request.POST['loginid']
        f = request.POST['fname']
        l = request.POST['lname']
        e = request.POST['email']
        m = request.POST['mob']
        add1 = request.POST['address1']
        add2 = request.POST['address2']
        c = request.POST['user_city']
        s = request.POST['user_state']
        co = request.POST['user_country']
        data.user.first_name = f
        data.user.last_name = l
        data.user.username = u
        data.user.email = e
        data.mobile = m
        data.add1 = add1
        data.add2 = add2
        data.country = co
        data.city = c
        data.state = s
        data.user.save()
        data.save()
        try:
            i = request.FILES['image']
            data.img = i
            data.save()
        except:
            pass
    d = {'data': data}

    return render(request, 'edittutor.html',d)

def EditQuestion(request,pid):
    if not request.user.is_authenticated:
        return redirect('tutorlogin')
    topic1 = Topic.objects.all()
    course1 = Course.objects.all()
    data = Question.objects.get(id=pid)
    if request.method == "POST":
        q = request.POST['fullQuestion']
        t = request.POST['topic']
        o1 = request.POST['option1']
        o2 = request.POST['option2']
        o3 = request.POST['option3']
        o4 = request.POST['option4']
        a = request.POST['answer']
        data.topic.topic=t
        data.question = q
        data.option1 = o1
        data.option2 = o2
        data.option3 = o3
        data.option4 = o4
        data.answer = a
        data.save()
    d = {'data':data,'course1':course1,'topic1':topic1}
    return render(request, 'editquestion.html',d)

def View_Result(request,pid):
    if not request.user.is_authenticated:
        return redirect('studentlogin')
    data1 = QuizResult.objects.get(id=pid)
    data = FinalResult.objects.filter(quiz=data1)
    d = {'data':data}
    return render(request,'viewresult.html',d)



def Signup_Student(request):
    error = ""
    if request.method == "POST":
        u = request.POST['loginid']
        f = request.POST['fname']
        l = request.POST['lname']
        p1 = request.POST['password']
        p2 = request.POST['cpassword']
        g = request.POST['gender']
        e = request.POST['email']
        m = request.POST['mob']
        d = request.POST['dob']
        add1 = request.POST['address1']
        add2 = request.POST['address2']
        c = request.POST['user_city']
        s = request.POST['user_state']
        co = request.POST['user_country']
        i = request.FILES['image']
        cat = "student"
        try:
            user = User.objects.create_user(username=u, first_name=f, last_name=l, password=p1, email=e)
            UserDetail.objects.create(user=user, cat=cat, gender=g, mobile=m, dob=d, add1=add1, add2=add2, city=c, state=s, country=co, img=i)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'signupstudent.html',d)


def Signup_Tutor(request):
    if request.method == "POST":
        u = request.POST['loginid']
        f = request.POST['fname']
        l = request.POST['lname']
        p1 = request.POST['password']
        p2 = request.POST['cpassword']
        g = request.POST['gender']
        e = request.POST['email']
        m = request.POST['mob']
        d = request.POST['dob']
        add1 = request.POST['address1']
        add2 = request.POST['address2']
        c = request.POST['user_city']
        s = request.POST['user_state']
        co = request.POST['user_country']
        i = request.FILES['image']
        cat = "tutor"

        user = User.objects.create_user(username=u, first_name=f, last_name=l, password=p1, email=e)
        UserDetail.objects.create(user=user, cat=cat, gender=g, mobile=m, dob=d, add1=add1, add2=add2, city=c, state=s, country=co, img=i)
        return redirect('tutorlogin')
    return render(request, 'signuptutor.html')

def ResultReport(request):
    if not request.user.is_authenticated:
        return redirect('tutorlogin')
    data = QuizResult.objects.all()
    d = {'data':data}
    return render(request,'resultreport.html',d)




