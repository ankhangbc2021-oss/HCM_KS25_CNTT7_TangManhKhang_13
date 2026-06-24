"""
HCM-KS25-CNTT7_Tăng Mạnh Khang_13
"""


def display_menu() -> str | int:
    """Hiển thị menu

    Returns:
        str | int: _description_
    """
    title = "=" * 15 + "MENU" + "=" * 15
    print(f"""
{title}
1. Hiển thị danh sách bách hóa
2. Thêm hàng hóa mới
3. Cập nhật hàng hóa
4. Xóa hàng hóa
5. Tìm kiếm hàng hóa
6. Thoát
{"="*len(title)}""")
    return input("Nhập lựa chọn của bạn: ").strip()


def get_input_validate(prompt: str, _type: str = "text") -> str | float | int:
    """Lấy và kiểm tra

    Args:
        prompt (str): _description_
        _type (str, optional): (float, quantity_int). Defaults to "text".

    Returns:
        str | float | int: _description_
    """
    while True:
        try:
            u_input = input(prompt).strip()
            if not u_input:
                raise ValueError("Dữ liệu không được để trống")

            if _type == "float":
                value_num = float(u_input)
                if value_num < 0:
                    raise ValueError("Dữ liệu phải >= 0")
                return value_num

            if _type == "quantity_int":
                value_num = int(u_input)
                if value_num < 0 or value_num > 100000:
                    raise ValueError("Số lượng tồn kho phải từ 0 - 100000")
                return value_num
            return u_input
        except ValueError as e:
            if "could not convert string to float" in str(e):
                print("[Lỗi]: Vui lòng nhập số. Nhập lại")

            elif "invalid literal for int" in str(e):
                print("[Lỗi]: Vui lòng nhập số nguyên. Nhập lại")

            else:
                print(f"[Lỗi]: {e}. Vui lòng nhập lại")


class InventoryItem:
    """Lớp mô tả"""

    def __init__(self, uid, name, category, quantity, unit_price, storage_fee):
        self.__id = uid.upper()
        self.__name = name.title()
        self.__category = category
        self.__quantity = quantity
        self.__unit_price = unit_price
        self.__storage_fee = storage_fee
        self.__total_inventory_value = 0
        self.__inventory_type = ""

    @property
    def id(self):
        """Hiển thị"""
        return self.__id

    @property
    def name(self):
        """Hiển thị"""
        return self.__name

    @property
    def category(self):
        """Hiển thị"""
        return self.__category

    @property
    def quantity(self):
        """Hiển thị"""
        return self.__quantity

    @property
    def unit_price(self):
        """Hiển thị"""
        return self.__unit_price

    @property
    def storage_fee(self):
        """Hiển thị"""
        return self.__storage_fee

    @property
    def total_inventory_value(self):
        """Hiển thị"""
        return self.__total_inventory_value

    @property
    def inventory_type(self):
        """Hiển thị"""
        return self.__inventory_type

    def update_quantity(self, new_quantity):
        """Cập nhật số lượng"""
        self.__quantity = new_quantity

    def update_unit_price(self, new_unit_price):
        """Cập nhật giá SP"""
        self.__unit_price = new_unit_price

    def update_storage_fee(self, new_storage_fee):
        """Cập nhật giá kho"""
        self.__storage_fee = new_storage_fee

    def calculate_inventory_value(self):
        """Cập nhật"""
        self.__total_inventory_value = (
            self.__quantity * self.__unit_price
        ) + self.__storage_fee

    def classify_inventoty(self):
        """Phân loại"""
        if self.__total_inventory_value > 50000000:
            self.__inventory_type = "Rất cao"
        elif self.__total_inventory_value > 20000000:
            self.__inventory_type = "Cao"
        elif self.__total_inventory_value > 5000000:
            self.__inventory_type = "Trung bình"
        else:
            self.__inventory_type = "Thấp"


class InventoryManager:
    """Lớp quản lý"""

    def __init__(self):
        self.items = []

    def add_item(self):
        """Thêm hàng"""
        item_id = get_input_validate("Nhập mã đơn hàng: ")
        for item in self.items:
            if item_id.lower() == getattr(item, "id").lower():
                print("Mã sản phẩm đã có")
                return

        item_name = get_input_validate("Nhập tên hàng hóa: ")
        item_category = get_input_validate("Nhập danh mục hàng hóa: ")
        item_quantity = get_input_validate("Nhập số lượng tồn kho: ", "quantity_int")
        item_price = get_input_validate("Nhập đơn giá: ", "float")
        item_store = get_input_validate("Nhập chi phí lưu kho: ", "float")

        new_item = InventoryItem(
            uid=item_id,
            name=item_name,
            category=item_category,
            quantity=item_quantity,
            unit_price=item_price,
            storage_fee=item_store,
        )

        self.items.append(new_item)
        new_item.calculate_inventory_value()
        new_item.classify_inventoty()
        print("Đã thêm thành công")

    def show_all(self, target: list = None):
        """Hiển thị"""
        list_show = self.items if target is None else target

        if not list_show:
            print("Danh sách hành hóa đang rỗng!")
            return

        title = (
            f"| {"Mã hàng hóa":<11} | "
            + f"{"Tên hàng hóa":<20} | "
            + f"{"Danh mục":<15} | "
            + f"{"Số lượng tồn kho":<20} | "
            + f"{"Đơn giá nhập":<20} | "
            + f"{"Chi phí lưu kho":<20} | "
            + f"{"Tổng giá trị tồn kho":<20} | "
            + f"{"Phân loại tồn kho":<18} |"
        )
        print("=" * len(title))
        print(f"{"Danh sách hàng hóa".upper():^170}")
        print("=" * len(title))
        print(title)
        print("-" * len(title))
        for item in list_show:
            print(
                f"| {getattr(item, "id"):<11} | "
                + f"{getattr(item, "name"):<20} | "
                + f"{getattr(item, "category"):<15} | "
                + f"{getattr(item, "quantity"):<20,} | "
                + f"{getattr(item, "unit_price"):<20,} | "
                + f"{getattr(item, "storage_fee"):<20,} | "
                + f"{getattr(item, "total_inventory_value"):<20,} | "
                + f"{getattr(item, "inventory_type"):<18} |"
            )
            print("-" * len(title))

    def update_item(self):
        """Cập nhật"""
        if not self.items:
            print("Danh sách hành hóa đang rỗng!")
            return

        search_id = get_input_validate("Nhập mã hàng cần cập nhật: ")
        for item in self.items:
            if search_id.lower() == getattr(item, "id").lower():
                print("Đã tìm thấy mã:", getattr(item, "id"))
                new_quantity = get_input_validate(
                    "Nhập số lượng tồn kho mới: ", "quantity_int"
                )
                new_price = get_input_validate("Nhập đơn giá mới: ", "float")
                new_store = get_input_validate("Nhập chi phí lưu kho mới: ", "float")

                item.update_quantity(new_quantity)
                item.update_unit_price(new_price)
                item.update_storage_fee(new_store)
                item.calculate_inventory_value()
                item.classify_inventoty()
                print("Đã cập nhật thành công")
                return
        print("Không tìm thấy hàng hóa cần cập nhật!")

    def delete_item(self):
        """Xóa hàng"""
        if not self.items:
            print("Danh sách hành hóa đang rỗng!")
            return

        search_id = get_input_validate("Nhập mã hàng cần cập xóa: ")
        for item in self.items:
            if search_id.lower() == getattr(item, "id").lower():
                print("Đã tìm thấy mã:", getattr(item, "id"))
                while True:
                    choice = input("Bạn có chắc muốn xóa hàng hóa này không? (Y/N)")
                    if choice.lower() == "y":
                        self.items.remove(item)
                        print("Đã xóa thành công")
                        return
                    elif choice.lower() == "n":
                        print("Đã hủy thao tác")
                        return
                    else:
                        print("Lựa chọn không hợp lệ")

        print("Không tìm thấy hàng hóa cần xóa!")

    def search_item(self):
        """Tìm kiếm"""
        if not self.items:
            print("Danh sách hành hóa đang rỗng!")
            return

        search_name = get_input_validate("Nhập tên hàng cần tìm: ")
        list_search = [
            item
            for item in self.items
            if search_name.lower() in getattr(item, "name").lower()
        ]
        if list_search:
            print(f"Đã tìm thấy {len(list_search)} hàng hóa phù hợp")
            self.show_all(list_search)
        else:
            print("Không tìm thấy hàng hóa phù hợp!")


def main():
    """Thực thi"""
    items = InventoryManager()

    while True:
        choice = display_menu()

        match choice:
            case "1":
                items.show_all()
            case "2":
                items.add_item()
            case "3":
                items.update_item()
            case "4":
                items.delete_item()
            case "5":
                items.search_item()
            case "6":
                print("Đã thoát")
                break
            case _:
                print("Vui lòng nhập 1-6")


if __name__ == "__main__":
    main()
