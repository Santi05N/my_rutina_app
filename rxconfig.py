import reflex as rx

config = rx.Config(
    app_name="my_rutina_app",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
    frontend_host="0.0.0.0",
)