import os
import sys
import tarfile
import urllib.request as urllib

baseURL = "http://www.ispd.cc/contests/19/benchmarks/"
target_dir = os.path.dirname(os.path.abspath(__file__))
filenames = [f"ispd19_test{i}.tgz" for i in range(1, 11)]
ispd19_dir = os.path.join(target_dir, "ispd2019")
try:
    os.mkdir(ispd19_dir)
except OSError:
    pass

for filename in filenames:
    file_url = baseURL + filename
    path_to_file = os.path.join(target_dir, filename)

    print("Download from %s to %s" % (file_url, path_to_file))
    response = urllib.urlopen(file_url)
    content = response.read()
    with open(path_to_file, 'wb') as f:
        f.write(content)

    print("Uncompress %s to %s" % (path_to_file, ispd19_dir))
    with tarfile.open(path_to_file, 'r:gz') as tar:
        tar.extractall(ispd19_dir, filter='data')

    print("remove downloaded file %s" % (path_to_file))
    os.remove(path_to_file)
