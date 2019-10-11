from google.cloud import datastore
import logging
import datetime

def auto_delete(request):
    if request.args and \
        'kind' in request.args and \
        'field' in request.args and \
        'interval' in request.args:

        db_client = datastore.Client()
        batch = db_client.batch()
        query = db_client.query(kind=request.args['kind'])

        interval = int(request.args['interval'])
        logging.info(f'Auto-deleting entities older than {interval} days')

        time_delta = (datetime.datetime.now() - datetime.timedelta(days=interval)).isoformat()
        query.add_filter(request.args['field'], '<=', time_delta)
        query.keys_only()
        entities = query.fetch()

        batch.begin()
        for entity in entities:
            batch.delete(entity.key)

        batch.commit()
    else:
        problem = {'type': 'MissingParameters',
                   'title': 'Expected kind, days interval and field for deleting entities not found',
                   'status': 400}
        response = make_response(jsonify(problem), 400)
        response.headers['Content-Type'] = 'application/problem+json',
        return response
