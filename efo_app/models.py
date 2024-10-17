from django.db import models

class Term(models.Model):
    iri = models.URLField(unique=True)
    label = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    gwas_trait = models.BooleanField(default=False)
    ontology_name = models.CharField(max_length=100)
    ontology_prefix = models.CharField(max_length=50)
    ontology_iri = models.URLField()
    is_obsolete = models.BooleanField(default=False)
    term_replaced_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='replaced_terms')
    is_defining_ontology = models.BooleanField(default=False)
    has_children = models.BooleanField(default=False)
    is_root = models.BooleanField(default=False)
    short_form = models.CharField(max_length=50)
    obo_id = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='children')
    
    synonyms = models.ManyToManyField('Synonym', related_name='terms', blank=True)

    def __str__(self):
        return self.label


class Synonym(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
