#!/usr/bin/python3
""" Test for the console """
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage
import os
from re import search
from models.base_model import BaseModel
import pep8


def serve_value(command):
    """ Return the sys output of the command given """
    with patch("sys.stdout", new=StringIO()) as res:
            HBNBCommand().onecmd(command)

    return res.getvalue()


class test_console(unittest.TestCase):
    """ Testing console output """
    def setUp(self):
        """ Prepare removing current file.json"""
        try:
            os.remove(os.getcwd() * "/file.json")
            FileStorage__objects = []
        except:
            pass

    def test_help(self):
        """ Test the command help from the terminal """

        result = serve_value("help")
        self.assertTrue("Documented commands (type help <topic>):" in result)
        self.assertTrue(search("EOF", result))
        self.assertIsNotNone(serve_value("help EOF"))
        self.assertTrue(search("all", result))
        self.assertIsNotNone(serve_value("help all"))
        self.assertTrue(search("count", result))
        self.assertIsNotNone(serve_value("help count"))
        self.assertTrue(search("create", result))
        self.assertIsNotNone(serve_value("help create"))
        self.assertTrue(search("destroy", result))
        self.assertIsNotNone(serve_value("help destroy"))
        self.assertTrue(search("quit", result))
        self.assertIsNotNone(serve_value("help quit"))
        self.assertTrue(search("show", result))
        self.assertIsNotNone(serve_value("help show"))
        self.assertTrue(search("update", result))
        self.assertIsNotNone(serve_value("help update"))

        self.assertEqual("*** No help on ME\n", serve_value("help ME"))

    def test_show(self):
        """ Test the command show from the terminal """
        test_obj = BaseModel()
        _id = test_obj.id
        res = serve_value(
            "show {} {}".format(test_obj.to_dict()["__class__"], test_obj.id))
        self.assertIsNotNone(res)
        self.assertTrue(test_obj.to_dict()["__class__"] in res)
        self.assertTrue(_id in res)
        self.assertTrue("created_at" in res)
        self.assertTrue("updated_at" in res)
        self.assertEqual(
            "** class doesn't exist **\n", serve_value("show x"))
        self.assertEqual(
            "** no instance found **\n", serve_value("show BaseModel x"))
        self.assertEqual(
            "** instance id missing **\n", serve_value("show BaseModel"))

    def test_codestyle(self):
        """ Test Py code stile """
        style = pep8.Checker('console.py')
        self.assertEqual(style.check_all(), 0)

    def test_docs(self):
        self.assertIsNotNone(__import__("console").__doc__)
        self.assertIsNotNone(__import__("console").isfloat.__doc__)
        self.assertIsNotNone(__import__("console").isint.__doc__)
        self.assertIsNotNone(__import__("console").get_patters.__doc__)
        self.assertIsNotNone(__import__("console").marshall.__doc__)
        self.assertIsNotNone(__import__("console").HBNBCommand.__doc__)
        self.assertIsNotNone(__import__("console").HBNBCommand.preloop.__doc__)
        self.assertIsNotNone(__import__("console").HBNBCommand.precmd.__doc__)
        self.assertIsNotNone(__import__(
            "console").HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(__import__(
            "console").HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(__import__(
            "console").HBNBCommand.do_count.__doc__)
        self.assertIsNotNone(__import__(
            "console").HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(__import__(
            "console").HBNBCommand.help_create.__doc__)
        self.assertIsNotNone(__import__(
            "console").HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(__import__(
            "console").HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(__import__(
            "console").HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(__import__(
            "console").HBNBCommand.help_destroy.__doc__)
        self.assertIsNotNone(__import__(
            "console").HBNBCommand.help_all.__doc__)
        self.assertIsNotNone(__import__(
            "console").HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(__import__(
            "console").HBNBCommand.help_update.__doc__)

    def test_count(self):
        models = []
        hoped = 45

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("count BaseModel")

        for m in range(45):
            models.append(BaseModel())

        hoped += int(output.getvalue())
        self.assertEqual(hoped, int(output.getvalue()) + 45)
