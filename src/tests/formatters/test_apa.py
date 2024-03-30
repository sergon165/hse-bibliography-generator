"""
Тестирование функций оформления списка источников по APA.
"""

from formatters.base import BaseCitationFormatter
from formatters.models import (
    BookModel,
    InternetResourceModel,
    ArticlesCollectionModel,
    DissertationModel,
    JournalModel,
)
from formatters.styles.apa import APABook, APAInternetResource, APACitationFormatter


class TestAPA:
    """
    Тестирование оформления списка источников согласно APA.
    """

    def test_book(self, book_model_fixture: BookModel) -> None:
        """
        Тестирование форматирования книги.

        :param BookModel book_model_fixture: Фикстура модели книги
        :return:
        """

        model = APABook(book_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. (2020). Наука как искусство. СПб.: Просвещение."
        )

    def test_internet_resource(
        self, internet_resource_model_fixture: InternetResourceModel
    ) -> None:
        """
        Тестирование форматирования интернет-ресурса.

        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :return:
        """

        model = APAInternetResource(internet_resource_model_fixture)

        assert (
            model.formatted
            == "Ведомости. Наука как искусство. URL: https://www.vedomosti.ru. Accessed 01.01.2021."
        )

    def test_citation_formatter(
        self,
        book_model_fixture: BookModel,
        internet_resource_model_fixture: InternetResourceModel,
        articles_collection_model_fixture: ArticlesCollectionModel,
        dissertation_model_fixture: DissertationModel,
        journal_model_fixture: JournalModel,
    ) -> None:
        """
        Тестирование функции итогового форматирования списка источников.

        :param BookModel book_model_fixture: Фикстура модели книги
        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :param DissertationModel dissertation_model_fixture: Фикстура модели диссертации
        :param JournalModel journal_model_fixture: Фикстура модели статьи из журнала
        :return:
        """

        models = [
            book_model_fixture,
            internet_resource_model_fixture,
            articles_collection_model_fixture,
            dissertation_model_fixture,
            journal_model_fixture,
        ]
        result = APACitationFormatter(models).format()

        # тестирование сортировки списка источников
        assert result[0].data == internet_resource_model_fixture
        assert result[1].data == book_model_fixture
