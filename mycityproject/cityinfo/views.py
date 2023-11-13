from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def home(request):
    cityName='Dnipro'
    return HttpResponse(f"""
    <h1>Hello from Django</h1>
    <h2>You are welcome in  {cityName}</h2>
    <img src='https://upload.wikimedia.org/wikipedia/commons/1/14/%D0%92%D0%B8%D0%B4_%D0%BD%D0%B0_%D0%BC%D1%96%D1%81%D1%82%D0%BE_%D0%B7%D1%96_%D1%81%D1%82%D0%BE%D1%80%D0%BE%D0%BD%D0%B8_%D0%9F%D1%96%D0%B2%D0%B4%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BC%D0%BE%D1%81%D1%82%D1%83.jpg'>
        <p><a href="/">Main</a></p>
        <p><a href="/news">News</a></p>
        <p><a href="/management">Management</a></p>
        <p><a href="/facts">Facts</a></p>
        <p><a href="/contacts">Contacts</a></p>
        <p><a href="/history">History</a></p>
        <p><a href="/history/people">People</a></p>
        <p><a href="/history/photos">Photos</a></p>
    """)

def news(request):
    return HttpResponse(f"""
    <h1>Welcome to Dnipro</h1>
    <h2>We have a new square in our city, we call it Uspenskaya ploscha</h2>
    <img src='https://opentv.media/wp-content/uploads/2021/06/1-30.jpg'>
    <p><a href="/">Main</a></p>
        <p><a href="/management">Management</a></p>
        <p><a href="/facts">Facts</a></p>
        <p><a href="/contacts">Contacts</a></p>
        <p><a href="/history">History</a></p>
        <p><a href="/history/people">People</a></p>
        <p><a href="/history/photos">Photos</a></p>
    """)

def management(request):
    return HttpResponse(f"""
    <h1>Welcome to Dnipro</h1>
    <h2>The manager of Dnipro is Boris Filatov</h2>
    <img src="https://ki.ill.in.ua/a/675x0/24201118.jpg">
    <p><a href="/">Main</a></p>
        <p><a href="/news">News</a></p>
        <p><a href="/facts">Facts</a></p>
        <p><a href="/contacts">Contacts</a></p>
        <p><a href="/history">History</a></p>
        <p><a href="/history/people">People</a></p>
        <p><a href="/history/photos">Photos</a></p>
    """)

def facts(request):
    return HttpResponse(f"""
        <h1>Welcome to Dnipro</h1>
        <h2>Dnipro is a primarily industrial city of around one million people. 
         It has developed into a large urban centre over the past few centuries to become, today, 
         Ukraine's fourth-largest city after Kyiv, Kharkiv and Odesa.
         Stalinist architecture (monumental soviet classicism) dominates in the city centre.</h2>
         <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/%D0%97%D0%B8%D0%BC%D0%BE%D0%B2%D0%B8%D0%B9_%D1%82%D0%B5%D0%B0%D1%82%D1%80.jpg/1920px-%D0%97%D0%B8%D0%BC%D0%BE%D0%B2%D0%B8%D0%B9_%D1%82%D0%B5%D0%B0%D1%82%D1%80.jpg">
        <p><a href="/">Main</a></p>
        <p><a href="/news">News</a></p>
        <p><a href="/management">Management</a></p>
        <p><a href="/contacts">Contacts</a></p>
        <p><a href="/history">History</a></p>
        <p><a href="/history/people">People</a></p>
        <p><a href="/history/photos">Photos</a></p>
        """)

def contacts(request):
    return HttpResponse(f"""
            <h1>Welcome to Dnipro</h1>
            <h2>The manager of Dnipro is Boris Filatov, you can write him in facebook</h2>
            <img src="https://img.pravda.com/images/doc/e/8/e80aa4d-filatov--dnipro-ova-.avif">
            <p><a href="/">Main</a></p>
        <p><a href="/news">News</a></p>
        <p><a href="/management">Management</a></p>
        <p><a href="/facts">Facts</a></p>
        <p><a href="/history">History</a></p>
        <p><a href="/history/people">People</a></p>
        <p><a href="/history/photos">Photos</a></p>
            """)

def history(request):
    return HttpResponse(f"""
            <h1>Welcome to Dnipro</h1>
            <h2>Archeological evidence suggests the site of the present city was settled by Cossack communities from at least 1524.
             Yekaterinoslav ("glory of Catherine") was established by decree of the Russian Empress Catherine the Great in 1787 
             as the administrative center. From the end of the 19th century, the town attracted foreign capital and an international,
              multi-ethnic workforce exploiting Kryvbas iron ore and Donbas coal.</h2>
              <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/%D0%9A%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%BE%D1%81%D0%BB%D0%B0%D0%B2-%D0%BD%D0%B0-%D0%9A%D0%B0%D1%80%D1%82%D1%96-%D0%A8%D1%83%D0%B1%D0%B5%D1%80%D1%82%D0%B0.jpg/1024px-%D0%9A%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%BE%D1%81%D0%BB%D0%B0%D0%B2-%D0%BD%D0%B0-%D0%9A%D0%B0%D1%80%D1%82%D1%96-%D0%A8%D1%83%D0%B1%D0%B5%D1%80%D1%82%D0%B0.jpg">
              <p><a href="/">Main</a></p>
        <p><a href="/news">News</a></p>
        <p><a href="/management">Management</a></p>
        <p><a href="/facts">Facts</a></p>
        <p><a href="/contacts">Contacts</a></p>
        <p><a href="/history/people">People</a></p>
        <p><a href="/history/photos">Photos</a></p>
            """)

def people(request):
    return HttpResponse(f"""
            <h1>Famous people of Dnipro</h1>
            <h2>Peter Arshinov (1886–1937) – Ukrainian anarchist revolutionary and intellectual, chronicled the history of the Makhnovshchina, a stateless anarchist society in Ukraine </h2>
               <h2> Helena Blavatsky (1831–1891) – founder of Theosophical Society.</h2>
              <h2>  Marina Maximilian (born 1987) – Israeli singer-songwriter and actress.</h2>
                <p><a href="/">Main</a></p>
        <p><a href="/news">News</a></p>
        <p><a href="/management">Management</a></p>
        <p><a href="/facts">Facts</a></p>
        <p><a href="/contacts">Contacts</a></p>
        <p><a href="/history">History</a></p>
        <p><a href="/history/photos">Photos</a></p>
            """)

def photos(request):
    return HttpResponse(f"""
            <h1> Dnipro is nice</h1>
            <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/%D0%94%D0%BE%D0%BC_%D0%BE%D1%80%D0%B3%D0%B0%D0%BD%D0%BD%D0%BE%D0%B9_%D0%BC%D1%83%D0%B7%D1%8B%D0%BA%D0%B8_%D0%94%D0%BD%D0%B5%D0%BF%D1%80%D0%BE%D0%BF%D0%B5%D1%82%D1%80%D0%BE%D0%B2%D1%81%D0%BA_1.JPG/330px-%D0%94%D0%BE%D0%BC_%D0%BE%D1%80%D0%B3%D0%B0%D0%BD%D0%BD%D0%BE%D0%B9_%D0%BC%D1%83%D0%B7%D1%8B%D0%BA%D0%B8_%D0%94%D0%BD%D0%B5%D0%BF%D1%80%D0%BE%D0%BF%D0%B5%D1%82%D1%80%D0%BE%D0%B2%D1%81%D0%BA_1.JPG'>
             <p><a href="/">Main</a></p>
        <p><a href="/news">News</a></p>
        <p><a href="/management">Management</a></p>
        <p><a href="/facts">Facts</a></p>
        <p><a href="/contacts">Contacts</a></p>
        <p><a href="/history">History</a></p>
        <p><a href="/history/people">People</a></p>
        
            
            
            """)