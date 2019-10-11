from google.cloud import datastore
import logging
import datetime

def process_approve(request):
    if request.args
        and 'kind' in request.args
        and 'field' in request.args
        and 'interval' in request.args:

        db_client = datastore.Client()
        query = db_client.query(kind=request.args['kind'])

        interval = int(request.args['interval'])
        logging.info(f'Auto-deleting entities older than {interval} days')

        time_delta = datetime.datetime.utcnow() - datetime.timedelta(days=interval)
        query.add_filter(request.args['field'], '<=', time_delta)
        query.keys_only()
        entities = query.fetch()

        db_client.delete_multi(entities)
    else:
        problem = {'type': 'MissingParameters',
                   'title': 'Expected kind, days interval and field for deleting entities not found',
                   'status': 400}
        response = make_response(jsonify(problem), 400)
        response.headers['Content-Type'] = 'application/problem+json',
        return response
