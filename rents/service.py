from django.db.models import Sum

from rents.beans import ProductBean
from rents.models import RatingModel, CommentsModel, UploadrentsModel


def getAllProducts():

    products = []

    for product in UploadrentsModel.objects.all():

        product.path = str(product.path).split("/")[1]

        comments = CommentsModel.objects.filter(product=product.id)

        rating = 0
        count=0

        for ratingmodel in RatingModel.objects.filter(product=product.id):
            rating=rating+int(ratingmodel.rating)
            count=count+1

        totalrating=0

        print("rating",rating)
        print("count", count)

        try:
            totalrating=int((rating / count))
        except Exception as e:
            print(e)

        print(totalrating)

        bean = ProductBean(product, comments,totalrating,product.description)

        products.append(bean)

    return products





