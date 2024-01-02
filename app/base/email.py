from dataclasses import dataclass


def concat_email(recipient: str, domain: str) -> str:
    return f'{recipient}@{domain}'


@dataclass
class EmailApi:
    domain: str

    def get_contact_email(self) -> str:
        return concat_email('kontakt', self.domain)

    def get_merch_email(self) -> str:
        return concat_email('merch', self.domain)

    def get_booking_email(self) -> str:
        return concat_email('booking', self.domain)

    def get_webmaster_email(self) -> str:
        return concat_email('webmaster', self.domain)

    def get_all_emails(self) -> dict[str, str]:
        return {
            'contact': self.get_contact_email(),
            'merch': self.get_merch_email(),
            'booking': self.get_booking_email(),
            'webmaster': self.get_webmaster_email()
        }
