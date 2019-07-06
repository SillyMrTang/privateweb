# -*- coding:utf-8 -*-
import codecs, re, json, uuid
from flask import render_template, url_for, redirect, request, jsonify, session, g, make_response
from sqlalchemy.sql import exists
from models import Article, Category, Tag, Status, Secret
from App import db, uid
from . import blog


@blog.route('/blog', methods=['GET'])
def get_blog():
    page = int(request.args.get('page', 1))
    paginate = db.session.query(Article).filter(Category.id == 8).order_by(db.desc(Article.articls_posttime)).paginate(
        page, 2)
    articles = paginate.items

    # categorys = db.session.query(Category).filter(Category.info == 'python').all()

    return render_template('blog.html', art=articles, pag=paginate)
