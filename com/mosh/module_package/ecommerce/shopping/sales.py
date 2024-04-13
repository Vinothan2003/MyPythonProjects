from com.mosh.module_package.ecommerce.contact import customer  # absolute import

# from contact package import methods(function) from customer module
# from ..contact import customer  # relative import

customer.information()

print("Sales initialized", __name__)


def calculate_total():
    print("Calculating total")


def calculate_items():
    print("calculating items")


if __name__ == "__main__":
    calculate_items()
    print("Sales is main module now", __name__)
