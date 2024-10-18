from django.core.management.base import BaseCommand
from efo_app.models import Term, Synonym
import requests

class Command(BaseCommand):
    help = 'Load initial data into the database'

    def handle(self, *args, **kwargs):
        # Fetch data from the API
        response = requests.get('https://www.ebi.ac.uk/ols/api/ontologies/efo/terms?size=100')
        
        if response.status_code != 200:
            self.stdout.write(self.style.ERROR('Failed to fetch data from the API'))
            return
        
        terms = response.json().get('_embedded', {}).get('terms', [])
        print(f"Loaded {len(terms)} terms from the API.")

        for term in terms:
            # Create the Term entry
            efo_term = Term.objects.create(
                iri=term['iri'],
                label=term['label'],
                description=', '.join(term.get('description', [])),
                gwas_trait=term.get('gwas_trait', False),
                ontology_name=term['ontology_name'],
                ontology_prefix=term['ontology_prefix'],
                ontology_iri=term['ontology_iri'],
                is_obsolete=term.get('is_obsolete', False),
                term_replaced_by=None,
                is_defining_ontology=term.get('is_defining_ontology', False),
                has_children=term.get('has_children', False),
                is_root=term.get('is_root', False),
                short_form=term.get('short_form', ''),
                obo_id=term.get('obo_id', ''),
            )
            self.stdout.write(self.style.SUCCESS(f'Created Term: {efo_term.label}'))

            # Handle synonyms if available
            synonyms = term.get('synonyms', [])
            for synonym in synonyms:
                synonym_obj, created = Synonym.objects.get_or_create(name=synonym)
                efo_term.synonyms.add(synonym_obj)  # Link the synonym to the term
                self.stdout.write(self.style.SUCCESS(f'Added Synonym: {synonym_obj.name} to Term: {efo_term.label}'))

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))

