class Testbun:
    def test_add_bun_name(self, create_bun):
        assert create_bun.get_name() == 'Кунжутная'

    def test_add_bun_price(self, create_bun):
        assert create_bun.get_price() == 100