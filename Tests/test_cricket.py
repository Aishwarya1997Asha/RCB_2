import pytest

from POM.details_cricket import Cricket


@pytest.mark.usefixtures("setup_file")
class Test_Cricket:
    @pytest.fixture(autouse=True)
    def SetUp(self, setup_file):
        self.file = setup_file
        self.cricket = Cricket(self.file)


    def test_cricket_player_validate(self):
        assert len(self.cricket.country_filter(country="india", not_in=True)) == 4


    def test_cricket_role_validate(self):
        assert len(self.cricket.role_filter(role="Wicket-keeper")) >= 1

