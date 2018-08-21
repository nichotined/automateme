from datadog import initialize, ThreadStats


class Metrics():
    def __init__(self):
        pass

    @staticmethod
    def send(metric_name: str, data_value: float, **kwargs):
        tags = ['metric_submission:threadstats']
        if kwargs:
            for key, value in kwargs.items():
                if 'tag' in key:
                    tags.append('{0}:{1}'.format(key[3:], value))

        options = {'api_key': '52ef848539fe3e746a1dc5d189c91315',
                   'app_key': '76b1154922c2beea61fa4aefbda3d639373e4a12'}

        initialize(**options)

        stats = ThreadStats()
        stats.start()
        stats.gauge(metric_name, value=data_value, tags=tags)

