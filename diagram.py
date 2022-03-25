from turtle import color
from diagrams import Cluster, Diagram
from diagrams.saas.cdn import Cloudflare
from diagrams.saas.media import Cloudinary
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.network import Traefik
from diagrams.azure.storage import BlobStorage
from diagrams.custom import Custom

graph_attr = {
    "fontsize": "30",
    "fontname": "Arial"
}

cluster_attr = {
    "fontname": "Arial",
    "fontsize": "15"
}

with Diagram("Photo Proofing", show=False, direction="TB", graph_attr=graph_attr):
    dns = Cloudflare("Cloudflare DNS")
    traefik = Traefik("Traefik: Reverse Proxy, Certificate Issuer, Monitoring")
    sendgrid = Custom("SendGrid Email", "./images/sendgrid.png")

    with Cluster("Docker", graph_attr=cluster_attr):
        client = Custom("Angular Client", "./images/angular.png")
        api = Custom(".NET 6 API w/EF6", "./images/.net.png")
        redis = Redis("Redis Cache")
        api - redis
        insight = Custom("RedisInsight", "./images/redisinsight.png")
        insight - redis
    api - Custom("PlanetScale DB", "./images/planetscale.png")
    api - BlobStorage("Azure Blob Storage")
    api - sendgrid
    client - api
    traefik - insight

    dns - traefik - client - Cloudinary("Cloudinary CDN") - api

    



