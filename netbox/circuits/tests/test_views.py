import datetime

from circuits.choices import *
from circuits.models import Circuit, CircuitType, Provider
from utilities.testing import StandardTestCases


class ProviderTestCase(StandardTestCases.Views):
    model = Provider

    @classmethod
    def setUpTestData(cls):

        Provider.objects.bulk_create([
            Provider(name='Provider 1', slug='provider-1', asn=65001),
            Provider(name='Provider 2', slug='provider-2', asn=65002),
            Provider(name='Provider 3', slug='provider-3', asn=65003),
        ])

        cls.form_data = {
            'name': 'Provider X',
            'slug': 'provider-x',
            'asn': 65123,
            'account': '1234',
            'portal_url': 'http://example.com/portal',
            'noc_contact': 'noc@example.com',
            'admin_contact': 'admin@example.com',
            'comments': 'Another provider',
            'tags': 'Alpha,Bravo,Charlie',
        }

        cls.csv_data = (
            "name,slug",
            "Provider 4,provider-4",
            "Provider 5,provider-5",
            "Provider 6,provider-6",
        )


class CircuitTypeTestCase(StandardTestCases.Views):
    model = CircuitType

    # Disable inapplicable tests
    test_get_object = None
    test_delete_object = None

    @classmethod
    def setUpTestData(cls):

        CircuitType.objects.bulk_create([
            CircuitType(name='Circuit Type 1', slug='circuit-type-1'),
            CircuitType(name='Circuit Type 2', slug='circuit-type-2'),
            CircuitType(name='Circuit Type 3', slug='circuit-type-3'),
        ])

        cls.form_data = {
            'name': 'Circuit Type X',
            'slug': 'circuit-type-x',
            'description': 'A new circuit type',
        }

        cls.csv_data = (
            "name,slug",
            "Circuit Type 4,circuit-type-4",
            "Circuit Type 5,circuit-type-5",
            "Circuit Type 6,circuit-type-6",
        )


class CircuitTestCase(StandardTestCases.Views):
    model = Circuit

    @classmethod
    def setUpTestData(cls):

        provider = Provider(name='Provider 1', slug='provider-1', asn=65001)
        provider.save()

        circuittype = CircuitType(name='Circuit Type 1', slug='circuit-type-1')
        circuittype.save()

        Circuit.objects.bulk_create([
            Circuit(cid='Circuit 1', provider=provider, type=circuittype),
            Circuit(cid='Circuit 2', provider=provider, type=circuittype),
            Circuit(cid='Circuit 3', provider=provider, type=circuittype),
        ])

        cls.form_data = {
            'cid': 'Circuit X',
            'provider': provider.pk,
            'type': circuittype.pk,
            'status': CircuitStatusChoices.STATUS_ACTIVE,
            'tenant': None,
            'install_date': datetime.date(2020, 1, 1),
            'commit_rate': 1000,
            'description': 'A new circuit',
            'comments': 'Some comments',
            'tags': 'Alpha,Bravo,Charlie',
        }

        cls.csv_data = (
            "cid,provider,type",
            "Circuit 4,Provider 1,Circuit Type 1",
            "Circuit 5,Provider 1,Circuit Type 1",
            "Circuit 6,Provider 1,Circuit Type 1",
        )
