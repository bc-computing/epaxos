import numpy

def calculate_statistics_for_data(data, cdf=True, cdf_log_precision=4):
    npdata = numpy.asarray(data)
    s = {
        'p50': numpy.percentile(npdata, 50).item(),
        'p75': numpy.percentile(npdata, 75).item(),
        'p90': numpy.percentile(npdata, 90).item(),
        'p95': numpy.percentile(npdata, 95).item(),
        'p99': numpy.percentile(npdata, 99).item(),
        'p99.9': numpy.percentile(npdata, 99.9).item(),
        'max': numpy.amax(npdata).item(),
        'min': numpy.amin(npdata).item(),
        'mean': numpy.mean(npdata).item(),
        'stddev': numpy.std(npdata).item(),
        'var': numpy.var(npdata).item(),
    }
    if cdf:
        s['cdf'] = calculate_cdf_for_npdata(npdata)
        s['cdf_log'] = calculate_cdf_log_for_npdata(npdata, cdf_log_precision)
    return s

def calculate_cdf_for_npdata(npdata):
    ptiles = []
    for i in range(1, 100): # compute percentiles [1, 100)
        ptiles.append([i, numpy.percentile(npdata, i, interpolation='higher')])
    return ptiles

def calculate_cdf_log_for_npdata(npdata, precision):
    ptiles = []
    base = 0
    scale = 1
    for i in range(0, precision):
        for j in range(0, 90):
            if i == 0 and j == 0:
                continue
            ptiles.append([base + j / scale, numpy.percentile(npdata, base + j / scale, interpolation='higher')])
        base += 90 / scale
        scale = scale * 10
    return ptiles