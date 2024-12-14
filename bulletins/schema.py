import graphene
from graphene_django import DjangoObjectType

from bulletins.models import Bulletin


class BulletinType(DjangoObjectType):
    """
    Тип GraphQL для модели Bulletin.

    Этот тип используется для представления объектов Bulletin в GraphQL API.

    Атрибуты:
        Meta (class): Внутренний класс, определяющий модель и поля, которые будут использоваться.
    """
    class Meta:
        model = Bulletin
        fields = ("id", "title", "description", "price", "hashtags")


class Query(graphene.ObjectType):
    """
    Основной класс запроса GraphQL.

    Этот класс определяет доступные запросы для получения данных о объявлениях.

    Атрибуты:
       all_bulletins (List[BulletinType]): Запрос для получения всех объявлений.
       bulletins_by_title (List[BulletinType]): Запрос для получения объявлений по названию.
       bulletins_by_hashtag (List[BulletinType]): Запрос для получения объявлений по хэштегу.
    """
    all_bulletins = graphene.List(BulletinType)
    bulletins_by_title = graphene.List(
        BulletinType, title=graphene.String(required=True)
    )
    bulletins_by_hashtag = graphene.List(
        BulletinType, hashtag=graphene.String(required=True)
    )

    def resolve_all_bulletins(self, info):
        """
        Решатель для запроса all_bulletins.

        Возвращает список всех объявлений из базы данных.

        Аргументы:
            info (ResolveInfo): Информация о контексте запроса.

        Возвращает:
            QuerySet: Список всех объектов Bulletin.
        """
        return Bulletin.objects.all()

    def resolve_bulletins_by_title(self, info, title):
        """
        Решатель для запроса bulletins_by_title.

        Возвращает список объявлений, название которых содержит указанный текст.

        Аргументы:
            info (ResolveInfo): Информация о контексте запроса.
            title (str): Название, по которому необходимо выполнить поиск.

        Возвращает:
            QuerySet: Список объектов Bulletin, соответствующих заданному названию.
        """
        return Bulletin.objects.filter(title__icontains=title)

    def resolve_bulletins_by_hashtag(self, info, hashtag):
        """
        Решатель для запроса bulletins_by_hashtag.

        Возвращает список объявлений, содержащих указанный хэштег.

        Аргументы:
            info (ResolveInfo): Информация о контексте запроса.
            hashtag (str): Хэштег, по которому необходимо выполнить поиск.

        Возвращает:
            QuerySet: Список объектов Bulletin, соответствующих заданному хэштегу.
        """
        # Удаляем символ # из хэштега, если он есть
        cleaned_hashtag = hashtag.lstrip('#')
        # Используем icontains для поиска по строке с хэштегами
        return Bulletin.objects.filter(hashtags__icontains=f'#{cleaned_hashtag}')


schema = graphene.Schema(query=Query)
