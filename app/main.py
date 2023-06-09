from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers_list: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    arr = []
    for item in customers_list:
        new_customer = Customer(name=item["name"], food=item["food"])
        arr.append(new_customer)
    hall = CinemaHall(number=hall_number)
    hall_cleaner = Cleaner(name=cleaner)
    cinema_bar = CinemaBar()
    for customer in arr:
        cinema_bar.sell_product(product=customer.food, customer=customer)
    hall.movie_session(
        movie_name=movie,
        customers=arr,
        cleaning_staff=hall_cleaner
    )
