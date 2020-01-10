from django.contrib import admin

from openzaak.utils.admin import AuditTrailAdminMixin, AuditTrailInlineAdminMixin

from .models import Besluit, BesluitInformatieObject


class BesluitInformatieObjectInline(AuditTrailInlineAdminMixin, admin.TabularInline):
    model = BesluitInformatieObject
    extra = 0
    readonly_fields = ("uuid",)
    raw_id_fields = ("_informatieobject",)
    viewset = (
        "openzaak.components.besluiten.api.viewsets.BesluitInformatieObjectViewSet"
    )


@admin.register(Besluit)
class BesluitAdmin(AuditTrailAdminMixin, admin.ModelAdmin):
    list_display = ("verantwoordelijke_organisatie", "identificatie", "datum")
    list_filter = ("datum", "ingangsdatum")
    date_hierarchy = "datum"
    search_fields = (
        "verantwoordelijke_organisatie",
        "identificatie",
        "uuid",
    )
    raw_id_fields = ("_besluittype", "_zaak")
    readonly_fields = ("uuid",)
    inlines = (BesluitInformatieObjectInline,)
    viewset = "openzaak.components.besluiten.api.viewsets.BesluitViewSet"


@admin.register(BesluitInformatieObject)
class BesluitInformatieObjectAdmin(AuditTrailAdminMixin, admin.ModelAdmin):
    list_display = ("besluit", "_informatieobject", "_informatieobject_url")
    viewset = (
        "openzaak.components.besluiten.api.viewsets.BesluitInformatieObjectViewSet"
    )
    readonly_fields = ("uuid",)
