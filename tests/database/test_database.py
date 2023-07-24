import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qn = db.select_product_qnt_by_id(1)
    # print(water_qn)

    assert water_qn[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, "печиво", "солодке", 30)
    product_qnt = db.select_product_qnt_by_id(4)
    # print(product_qnt)

    assert product_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, "тестові", "дані", 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    # print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"


# Individual:


@pytest.mark.db_ind
def test_update_product_qnt_by_name():
    db = Database()
    db.update_product_qnt_by_name("молоко", 15)
    milk = db.select_product_qnt_by_id(3)
    # print(milk)

    assert milk[0][0] == 15


@pytest.mark.db_ind
def test_insert_order_verify():
    db = Database()
    db.insert_new_order(2, 1, 1, "15:35:12")
    new_order = db.get_order_details(2)

    assert new_order[0][0] == 2
    assert new_order[0][1] == 1
    assert new_order[0][2] == 1
    assert new_order[0][3] == "15:35:12"


@pytest.mark.db_ind
def test_check_name_by_order():
    db = Database()
    report = db.get_customer_name_by_order(1)

    assert report[0][1] == "Sergii"


@pytest.mark.db_ind
def test_check_product_details_by_order():
    db = Database()
    report = db.get_product_details_by_order(2)

    assert report[0][1] == "солодка вода"
    assert report[0][2] == "з цукром"


@pytest.mark.db_ind
def test_insert_next_order_check():
    db = Database()
    next_id = db.get_order_next_id()
    db.insert_next_order(next_id, 2, 2, "18:14:51")
    next_order = db.get_order_details(next_id)
    # print(next_id)
    # print(next_order)

    assert next_order[0][0] == next_id
    assert next_order[0][1] == 2
    assert next_order[0][2] == 2
    assert next_order[0][3] == "18:14:51"

    db.delete_order_by_id(next_id)


@pytest.mark.db_ind
def test_product_names():
    db = Database()
    names = db.get_all_product_names()

    assert names[0][0] == "солодка вода"
    assert names[1][0] == "солодка вода"
    assert names[2][0] == "молоко"
    assert names[3][0] == "печиво"


@pytest.mark.db_ind
def test_product_names_lenght():
    db = Database()
    names = db.get_all_product_names()

    # Check that all product names are shorter than 16 chr

    result = True

    for n in range(0, len(names) - 1):
        if len(names[n][0]) > 15:
            result = False

    assert result == True


@pytest.mark.db_ind
def test_product_cookie_quantity():
    db = Database()
    qnt = db.get_product_quantity("печиво")
    # print(qnt)

    assert qnt[0][0] == 30
