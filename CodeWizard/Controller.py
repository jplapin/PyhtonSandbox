import web

urls = (
    '/', 'home',
    '/register', 'registerclick'
)

render = web.template.render("views/templates", base="MainLayout")
app = web.application(urls, globals())

# Classes/Routes
class home:
    def GET(self):
        return render.home()


class registerclick:
    def GET(self):
        return render.register()


if __name__ == "__main__":
    app.run()
