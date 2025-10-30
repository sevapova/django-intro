from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import redirect

def index_view(request: HttpRequest) -> HttpResponse:
    content = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Djumanov — Personal Website</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50 text-gray-800">

  <!-- Navbar -->
  <header class="flex justify-between items-center p-6 max-w-6xl mx-auto">
    <h1 class="text-2xl font-bold text-indigo-600">Djumanov</h1>
    <nav class="space-x-6 text-gray-700">
      <a href="#home" class="hover:text-indigo-600">Home</a>
      <a href="#about" class="hover:text-indigo-600">About</a>
      <a href="#projects" class="hover:text-indigo-600">Projects</a>
      <a href="#contact" class="hover:text-indigo-600">Contact</a>
    </nav>
  </header>

  <!-- Hero Section -->
  <section id="home" class="text-center py-24 px-4 bg-gradient-to-b from-indigo-50 to-white">
    <h2 class="text-4xl sm:text-5xl font-bold text-gray-800 mb-4">Hi, I'm <span class="text-indigo-600">Djumanov</span></h2>
    <p class="text-lg text-gray-600 mb-8 max-w-xl mx-auto">A passionate developer who loves building web apps, learning new technologies, and creating meaningful digital experiences.</p>
    <a href="#projects" class="bg-indigo-600 text-white px-6 py-3 rounded-full shadow hover:bg-indigo-700 transition">View My Work</a>
  </section>

  <!-- About Section -->
  <section id="about" class="max-w-4xl mx-auto py-16 px-4">
    <h3 class="text-3xl font-semibold text-center mb-8">About Me</h3>
    <p class="text-gray-700 leading-relaxed text-center">
      I’m a web developer with experience in <strong>Django</strong>, <strong>FastAPI</strong>, and modern frontend tools.
      I enjoy designing elegant solutions to complex problems and always strive to write clean, efficient, and scalable code.
    </p>
  </section>

  <!-- Projects Section -->
  <section id="projects" class="bg-gray-100 py-16 px-4">
    <h3 class="text-3xl font-semibold text-center mb-10">Projects</h3>
    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto">
      <div class="bg-white p-6 rounded-2xl shadow hover:shadow-lg transition">
        <h4 class="font-bold text-lg mb-2">Portfolio Website</h4>
        <p class="text-gray-600">A personal portfolio built with Django and TailwindCSS.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow hover:shadow-lg transition">
        <h4 class="font-bold text-lg mb-2">FastAPI Book API</h4>
        <p class="text-gray-600">A REST API for managing books with PostgreSQL and JWT authentication.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow hover:shadow-lg transition">
        <h4 class="font-bold text-lg mb-2">Todo App</h4>
        <p class="text-gray-600">A simple task manager built with React and Django REST Framework.</p>
      </div>
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact" class="max-w-4xl mx-auto py-16 px-4 text-center">
    <h3 class="text-3xl font-semibold mb-8">Get in Touch</h3>
    <p class="text-gray-600 mb-6">Want to collaborate or just say hi? Feel free to reach out!</p>
    <a href="mailto:djumanov@example.com" class="bg-indigo-600 text-white px-6 py-3 rounded-full hover:bg-indigo-700 transition">Say Hello</a>
  </section>

  <!-- Footer -->
  <footer class="text-center py-6 border-t text-gray-500 text-sm">
    © 2025 Djumanov. All rights reserved.
  </footer>

</body>
</html>
'''
    return HttpResponse(content=content)

def root_view(request: HttpRequest) -> HttpResponse:
    from django.shortcuts import redirect
    return redirect('/index/')

def home_view(request: HttpRequest) -> HttpResponse:
    params = request.GET

    a = int(params.get('a', 0))
    b = int(params.get('b', 0))

    result = a + b

    return HttpResponse(f'<h1>Result: {result}</h1>')

def about_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>About</h1>')

def projects_view(request: HttpRequest) -> HttpResponse:
    html = """
    <h1>Projects</h1>
    <ul>
        <li>Portfolio Website</li>
        <li>FastAPI Book API</li>
        <li>Todo App</li>
    </ul>
    """
    return HttpResponse(html)

def contact_view(request: HttpRequest) -> HttpResponse:
    html = """
    <h1>Contact</h1>
    <p>You can reach me at: <a href='mailto:sevaralatipova2307@gmail.com'>sevaralatipova2307@gmail.com</a></p>
    """
    return HttpResponse(html)

def greeting_view(
        request: HttpRequest,
        name: str
    ) -> HttpResponse:
    
    return HttpResponse(f'<h1>Salom, {name.title()}</h1>')

def get_products_view(
        request: HttpRequest,
        product_id: int
    ) -> HttpResponse:
    
    return JsonResponse({'message': 'ok'})

