import web

# the (.*) means that accept everything after the slash
urls = (
    "/(.*)/(.*)", "index"
)

# app = web.application(urls, globals())
render = web.template.render("resources/")


class index:
    def GET(self, name, age):
        return render.main(name, age)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
