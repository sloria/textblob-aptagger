# -*- coding: utf-8 -*-
import os
from invoke import task, run

@task
def test():
    run("python run_tests.py", pty=True)

@task
def clean():
    run("rm -rf build")
    run("rm -rf dist")
    run("rm -rf textblob_fr.egg-info")
    print("Cleaned up.")
