#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
{
    'name': 'Sale',
    'name_de_DE': 'Verkauf',
    'name_fr_FR': 'Vente',
    'version': '0.0.1',
    'author': 'B2CK',
    'email': 'info@b2ck.com',
    'website': 'http://www.tryton.org/',
    'category': 'Sale',
    'description': '''Define sale order.
Add to product sale informations.
Define the sale price as the list price.

With the possibilities:
    - to follow invoice and packing states from the sale order.
    - to define invoice method:
        - Manual
        - On Order Confirmed
        - On packing Sent
    - to define packing method:
        - Manual
        - On Order Confirmed
        - On Invoice Paid
''',
    'description_de_DE': ''' - Dient der Erstellung von Verkaufsvorgängen (Entwurf, Angebot, Auftrag).
 - Fügt den Artikeln Einkaufsinformationen hinzu.
 - Erlaubt die Definition des Einkaufspreises als Listenpreis.

Ermöglicht:
    - die Verfolgung des Status von Rechnungsstellung und Versand für Verkäufe
    - die Festlegung der Methode für die Rechnungsstellung:
        - Manuell
        - Nach Auftragsbestätigung
        - Nach Versand
    - die Festlegung der Methode für den Versand:
        - Manuell
        - Nach Auftragsbestätigung
        - Nach Bezahlung
''',
    'description_fr_FR': '''Défini l'ordre de vente.
Ajoute au produit les information de vente.

Avec la possibilité:
    ' de suivre l'état de la facture et du colisage depuis l'ordre de vente
    ' de choisir entre plusieurs méthodes de facturation:
        ' Manuelle
        ' Sur confirmation de la commande
        ' À la livraison
    ' de choisir entre plusieurs méthodes de colisage:
        ' Manuel
        ' Sur confirmation de la commande
        ' Au paiement de la facture
''',

    'depends': [
        'company',
        'party',
        'stock',
        'account',
        'product',
        'account_invoice',
        'workflow',
        'res',
        'ir',
        'currency',
        'account_product',
    ],
    'xml': [
        'sale.xml',
    ],
    'translation': [
        'de_DE.csv',
        'es_ES.csv',
        'fr_FR.csv',
    ],
}
