# -*- coding:utf-8 -*-
import codecs, re, json, uuid
from flask import render_template, url_for, redirect, request, jsonify, session, g, make_response
from sqlalchemy.sql import exists
from models import Article, Category, Tag, Status, Secret
from App import db, uid
from . import detail


@detail.route('/detail', methods=['GET'])
def detail():

    return render_template('detail.html')
