from rest_framework import serializers
from .models import Term, Synonym

class SynonymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Synonym
        fields = ['id', 'name']


class TermSerializer(serializers.ModelSerializer):
    synonyms = SynonymSerializer(many=True, read_only=True)  
    term_replaced_by = serializers.SerializerMethodField()  
    parent = serializers.SerializerMethodField()

    class Meta:
        model = Term
        fields = [
            'id', 'iri', 'label', 'description', 'gwas_trait', 'ontology_name', 'ontology_prefix',
            'ontology_iri', 'is_obsolete', 'term_replaced_by', 'is_defining_ontology', 'has_children',
            'is_root', 'short_form', 'obo_id', 'created_at', 'updated_at', 'parent', 'synonyms'
        ]

    def get_term_replaced_by(self, obj):
        if obj.term_replaced_by:
            return TermSerializer(obj.term_replaced_by).data
        return None

    def get_parent(self, obj):
        if obj.parent:
            return TermSerializer(obj.parent).data
        return None
