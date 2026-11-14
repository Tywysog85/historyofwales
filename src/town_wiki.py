"""The English Wikipedia article for each town page (towns.html and town-<slug>.html), keyed by the town's English name.
A town not listed here uses its English name, with spaces as underscores."""

WIKI = {
    "Bala": "Bala,_Gwynedd", "Bangor": "Bangor,_Gwynedd", "Bethesda": "Bethesda,_Gwynedd", "Nefyn": "Nefyn",
    "Flint": "Flint,_Flintshire", "Mold": "Mold,_Flintshire", "Holywell": "Holywell,_Flintshire", "Buckley": "Buckley,_Flintshire",
    "Newtown": "Newtown,_Powys", "Montgomery": "Montgomery,_Powys", "Knighton": "Knighton,_Powys", "Hay-on-Wye": "Hay-on-Wye",
    "Cardigan": "Cardigan,_Ceredigion", "New Quay": "New_Quay", "Llanbadarn Fawr": "Llanbadarn_Fawr,_Ceredigion",
    "Pembroke": "Pembroke,_Pembrokeshire", "Newport (Pembrokeshire)": "Newport,_Pembrokeshire", "Narberth": "Narberth,_Pembrokeshire",
    "Mumbles": "Mumbles", "Barry": "Barry,_Vale_of_Glamorgan", "Blackwood": "Blackwood,_Caerphilly", "Newport": "Newport,_Wales",
    "Llanfaches": "Llanvaches", "Holt": "Holt,_Wrexham", "Clydach": "Clydach,_Swansea", "Nelson": "Nelson,_Caerphilly",
    "Porth": "Porth", "Margam": "Margam", "Overton-on-Dee": "Overton-on-Dee", "Usk": "Usk", "Raglan": "Raglan,_Monmouthshire",
    "Tintern": "Tintern", "Caerwys": "Caerwys", "Llandybie": "Llandybie", "Pumsaint": "Pumsaint", "Tywyn": "Tywyn",
    "Aberdyfi": "Aberdyfi", "Conwy": "Conwy", "St Davids": "St_Davids", "St Asaph": "St_Asaph", "St Fagans": "St_Fagans",
    "St Clears": "St_Clears", "Llanfairpwllgwyngyll": "Llanfairpwllgwyngyll", "Flemingston": "Flemingston",
    "Neyland": "Neyland", "Loughor": "Loughor", "Rhymney": "Rhymney", "Gresford": "Gresford", "Ruabon": "Ruabon",
    "Penmynydd": "Penmynydd", "Aberffraw": "Aberffraw", "Llandaff": "Llandaff", "Senghenydd": "Senghenydd",
    "Rhosllannerchrugog": "Rhosllannerchrugog", "Crymych": "Crymych", "Mynachlog-ddu": "Mynachlog-ddu",
}


def wiki(en):
    return WIKI.get(en, en.replace(" ", "_"))
