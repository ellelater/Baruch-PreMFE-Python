import random
import math


def generate_normal(size, mean, std):
    return [random.normalvariate(mean, std) for i in xrange(size)]


def frequency(samples, lower_bound, upper_bound, num_bins):
    if num_bins <= 2:
        raise ValueError("Number of bins needs to be larger than 2")
    bin_width = (upper_bound - lower_bound) / (num_bins - 2)
    bins = [x * bin_width + lower_bound-bin_width/2 for x in xrange(num_bins)]
    count = [0] * num_bins
    for x in samples:
        if x <= lower_bound:
            count[0] += 1
        elif x >= upper_bound:
            count[-1] += 1
        else:
            bin = int(math.floor((x - lower_bound) / bin_width)) + 1
            count[bin] += 1
    return bins, count


def rescale(freq, new_mx=100., new_mn=1.):
    mn = min(freq) * 1.0
    mx = max(freq) * 1.0
    return [(new_mx - new_mn)/(mx - mn) * (x - mn) + new_mn for x in freq]


def draw_hist(values, freq):
    for x, count in zip(values, freq):
        print "{:.3f}: {}".format(x, '-'*int(round(count)))


def main():
    samples = generate_normal(2000, 10, 7)  # switch generation methods and bins to get other histograms
    bins, freq = frequency(samples, -11., 31., 100)  # normal distribution bounds: mean +- 3*std
    normal_freq = rescale(freq)
    draw_hist(bins, normal_freq)


if __name__ == '__main__':
    main()
