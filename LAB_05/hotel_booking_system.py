"""Hotel room reservation and booking management module."""

import hashlib
import hmac
import secrets
from pathlib import Path


ROOM_INVENTORY = {
    "101": {"type": "Deluxe", "price": 150.0, "is_booked": False},
    "102": {"type": "Suite", "price": 300.0, "is_booked": True},
    "103": {"type": "Standard", "price": 90.0, "is_booked": False},
}


def book_room(room_num, guest_name, booking_log=None):
    """Reserve an available room and optionally append an audit entry."""
    if booking_log is None:
        booking_log = []

    room = ROOM_INVENTORY.get(room_num)

    if room is None or room["is_booked"]:
        return False

    room["is_booked"] = True
    booking_log.append(
        f"Reserved room {room_num} for guest {guest_name}"
    )
    return True


def cancel_booking(room_num):
    """Cancel a booking, returning False when the room does not exist."""
    room = ROOM_INVENTORY.get(room_num)

    if room is None:
        return False

    room["is_booked"] = False
    return True


def check_room_status(room_num):
    """Return True when the requested room exists and is available."""
    room = ROOM_INVENTORY.get(room_num)
    return room is not None and not room["is_booked"]


def compute_seasonal_rate(room_num, multiplier=1.0):
    """Compute a seasonal room rate using a validated numeric multiplier."""
    room = ROOM_INVENTORY.get(room_num)

    if room is None:
        raise ValueError(f"Unknown room number: {room_num}")

    if (
        not isinstance(multiplier, (int, float))
        or isinstance(multiplier, bool)
    ):
        raise TypeError("The rate multiplier must be a number")

    if not 0.0 < multiplier <= 10.0:
        raise ValueError(
            "The rate multiplier must be greater than 0 and at most 10"
        )

    return room["price"] * multiplier


def generate_guest_hash(guest_id):
    """Generate a SHA-256 digest for a guest identifier."""
    return hashlib.sha256(
        guest_id.encode("utf-8")
    ).hexdigest()


def verify_guest_hash(guest_id, expected_digest):
    """Safely compare a guest identifier digest."""
    return hmac.compare_digest(
        generate_guest_hash(guest_id),
        expected_digest
    )


def generate_booking_ref():
    """Generate a cryptographically strong booking reference."""
    return secrets.randbelow(9000) + 1000


def export_room_ledger(filename="hotel_ledger.txt"):
    """Export room inventory to a text ledger."""
    ledger_path = Path(filename)

    ledger_path.write_text(
        f"{ROOM_INVENTORY}\n",
        encoding="utf-8"
    )

    return ledger_path.resolve()


def main():
    """Run a demonstration of the hotel booking functions."""
    book_room("101", "Emma Watson")
    cancel_booking("102")

    print(
        "Is 103 available:",
        check_room_status("103")
    )

    print(
        "Surge price:",
        compute_seasonal_rate("101", 1.25)
    )

    guest_digest = generate_guest_hash("GUEST_991")

    print("Guest Hash:", guest_digest)
    print("Booking Reference:", generate_booking_ref())
    print("Ledger exported to:", export_room_ledger())


if __name__ == "__main__":
    main()
