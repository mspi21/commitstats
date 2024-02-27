#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from collections import Counter
from sys import argv

def parse_args() -> str: #tuple[str, str]:
	in_file = argv[1]
	#out_file = argv[2]

	return in_file#, out_file

def filter_bots(commit):
	return not commit['author_name'].endswith('[bot]')

def plot_counts_to_file(iterable, title, outfile):
	ctr = Counter(iterable)

	HOW_MANY = 50

	ctr = {k: v for k,v in ctr.most_common(HOW_MANY)}

	plt.figure(figsize=(14, 6))
	plt.bar(ctr.keys(), ctr.values()) #list(map(math.log2, ctr.values())))

	cnt_total = len(set(iterable))
	cnt_shown = min(HOW_MANY, cnt_total)
	plt.title(f'{title} (Shown top {cnt_shown} from total {cnt_total}, total # commits = {len(iterable)})')
	plt.xticks(rotation='vertical')
	plt.savefig(outfile, bbox_inches='tight')

if __name__ == '__main__':
	in_file = parse_args()
	out_file = in_file.removesuffix('.json')
		
	df = pd.read_json(in_file)

	# Filter out bots, such as dependabot.
	bi = df.apply(filter_bots, axis=1)
	df = df[bi]

	sns.set_theme()
	plot_counts_to_file(df['author_name'], 'Commit authorship', f'{out_file}_authors.png')
	plot_counts_to_file(df['committer_name'], 'Commit approval/merge', f'{out_file}_committers.png')
