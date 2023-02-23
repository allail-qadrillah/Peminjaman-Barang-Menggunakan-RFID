from flask import Blueprint, render_template, redirect, url_for, request

views = Blueprint('views', __name__)


@views.route('/', methods=['POST', 'GET'])
def dashboard():
    return render_template('dashboard.html')


@views.route('/input-dosen', methods=['POST', 'GET'])
def input_dosen():
    return render_template('input_dosen.html')

@views.route('/data-dosen', methods=['POST', 'GET'])
def data_dosen():
    return render_template('data_dosen.html')


@views.route('/input-ruang', methods=['POST', 'GET'])
def input_ruang():
    return render_template('input_ruang.html')

@views.route('/data-ruang', methods=['POST', 'GET'])
def data_ruang():
    return render_template('data_ruang.html')


@views.route('/input-fakultas', methods=['POST', 'GET'])
def input_fakultas():
    return render_template('input_fakultas.html')

@views.route('/data-fakultas', methods=['POST', 'GET'])
def data_fakultas():
    return render_template('data_fakultas.html')


@views.route('/input-jurusan', methods=['POST', 'GET'])
def input_jurusan():
    return render_template('input_jurusan.html')

@views.route('/data-jurusan', methods=['POST', 'GET'])
def data_jurusan():
    return render_template('data_jurusan.html')


@views.route('/input-mahasiswa', methods=['POST', 'GET'])
def input_mahasiswa():
    return render_template('input_mahasiswa.html')

@views.route('/data-mahasiswa', methods=['POST', 'GET'])
def data_mahasiswa():
    return render_template('data_mahasiswa.html')


@views.route('/input-matakuliah', methods=['POST', 'GET'])
def input_matakuliah():
    return render_template('input_matakuliah.html')

@views.route('/data-matakuliah', methods=['POST', 'GET'])
def data_matakuliah():
    return render_template('data_matakuliah.html')


@views.route('/input-proyektor', methods=['POST', 'GET'])
def input_proyektor():
    return render_template('input_proyektor.html')

@views.route('/data-proyektor', methods=['POST', 'GET'])
def data_proyektor():
    return render_template('data_proyektor.html')
