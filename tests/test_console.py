#!/usr/bin/python3

"""This module tests the Console"""

import unittest
import pep8
import os
import json
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel


class TestConsole(unittest.TestCase):
    """Test cases for the console"""

    def setUp(self):
        """Set up test methods"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down test methods"""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_pep8_console(self):
        """Test for pep8"""
        style = pep8.StyleGuide()
        result = style.check_files(["console.py"])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_pep8_console_test(self):
        """Test for pep8"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(["tests/test_console.py"])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_docstrings_in_console(self):
        """Test for docstrings"""
        self.assertIsNotNone(HBNBCommand.__doc__)

    def test_docstrings_in_test_console(self):
        """Test for docstrings"""
        self.assertIsNotNone(HBNBCommand.__doc__)


class TestConsolePrompt(unittest.TestCase):
    """Test cases for the console prompt"""

    def setUp(self):
        """Set up test methods"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down test methods"""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_prompt(self):
        """Test for prompt"""
        self.assertEqual("(hbnb) ", self.console.prompt)

    def test_prompt_type(self):
        """Test for prompt type"""
        self.assertEqual(type(self.console.prompt), str)

    def test_empty_line(self):
        """Test for empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("\n")
            self.assertEqual("", f.getvalue().strip())


class TestConsoleHelp(unittest.TestCase):
    """Test cases for the console help command"""

    def setUp(self):
        """Set up test methods"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down test methods"""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_help(self):
        """Test for help"""
        help = ("Documented commands (type help <topic>):\n"
                "========================================\n"
                "EOF  all  create  destroy  help  quit  show  update")

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_EOF(self):
        """Test for help EOF"""
        help = "EOF command to exit the program"

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_all(self):
        """Test for help all"""
        help = "Prints all string representation of all instances"

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_create(self):
        """Test for help create"""
        help = "Creates a new instance of BaseModel"

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_destroy(self):
        """Test for help destroy"""
        help = "Deletes instance based on class name and id"

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(help, f.getvalue().strip())


class TestConsoleExit(unittest.TestCase):
    """Test cases for the console exit command"""

    def setUp(self):
        """Set up test methods"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down test methods"""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_exit(self):
        """Test for exit"""
        self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_exit_with_EOF(self):
        """Test for exit with EOF"""
        self.assertTrue(HBNBCommand().onecmd("EOF"))


class TestConsoleCreate(unittest.TestCase):
    """Test cases for the console create command"""

    def setUp(self):
        """Set up test methods"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down test methods"""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_create(self):
        """Test for create"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual("** class name missing **", f.getvalue().strip())

    def test_create_with_class(self):
        """Test for create with class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertRegex(f.getvalue().strip(),
                             r"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}")

    def test_create_with_class_invalid(self):
        """Test for create with class invalid"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())


class TestConsoleShow(unittest.TestCase):
    """Test cases for the console show command"""

    def setUp(self):
        """Set up test methods"""
        self.console = HBNBCommand()
        self.b1 = BaseModel()
        self.b1.save()
        self.b1_id = self.b1.id

    def tearDown(self):
        """Tear down test methods"""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_show(self):
        """Test for show"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual("** class name missing **", f.getvalue().strip())

    def test_show_with_class(self):
        """Test for show with class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual("** instance id missing **", f.getvalue().strip())

    def test_show_with_class_id(self):
        """Test for show with class id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel {}"
                                                  .format(self.b1_id)))
            self.assertEqual(str(self.b1), f.getvalue().strip())

    def test_show_with_class_id_invalid(self):
        """Test for show with class id invalid"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel 123456"))
            self.assertEqual("** no instance found **", f.getvalue().strip())

    def test_show_with_class_invalid_id(self):
        """Test for show with class invalid id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel 123456"))
            self.assertEqual("** no instance found **", f.getvalue().strip())

    def test_show_with_class_invalid_id_invalid(self):
        """Test for show with class invalid id invalid"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel MyModel"))
            self.assertEqual("** no instance found **", f.getvalue().strip())


class TestConsoleDestroy(unittest.TestCase):
    """Test cases for the console destroy command"""

    def setUp(self):
        """Set up test methods"""
        self.console = HBNBCommand()
        self.b1 = BaseModel()
        self.b1.save()
        self.b1_id = self.b1.id

    def tearDown(self):
        """Tear down test methods"""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_destroy(self):
        """Test for destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual("** class name missing **", f.getvalue().strip())

    def test_destroy_with_class(self):
        """Test for destroy with class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual("** instance id missing **", f.getvalue().strip())

    def test_destroy_with_class_id(self):
        """Test for destroy with class id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel {}"
                                                  .format(self.b1_id)))
            self.assertEqual("", f.getvalue().strip())

    def test_destroy_with_class_id_invalid(self):
        """Test for destroy with class id invalid"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 123456"))
            self.assertEqual("** no instance found **", f.getvalue().strip())

    def test_destroy_with_class_invalid_id(self):
        """Test for destroy with class invalid id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 123456"))
            self.assertEqual("** no instance found **", f.getvalue().strip())

    def test_destroy_with_class_invalid_id_invalid(self):
        """Test for destroy with class invalid id invalid"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel MyModel"))
            self.assertEqual("** no instance found **", f.getvalue().strip())


class TestConsoleAll(unittest.TestCase):
    """Test cases for the console all command"""

    def setUp(self):
        """Set up test methods"""
        self.console = HBNBCommand()
        self.b1 = BaseModel()
        self.b1.save()
        self.b1_id = self.b1.id

    def tearDown(self):
        """Tear down test methods"""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_all_object(self):
        """Test for all object"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_all_with_class(self):
        """Test for all with class invalid"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
            self.assertIn("BaseModel", f.getvalue().strip())

    def test_all_with_class_invalid(self):
        """Test for all with class invalid"""
        invalid = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            self.assertEqual(invalid, f.getvalue().strip())


class TestConsoleUpdate(unittest.TestCase):
    """Test cases for the console update command"""

    def setUp(self):
        """Set up test methods"""
        self.console = HBNBCommand()
        self.b1 = BaseModel()
        self.b1.save()
        self.b1_id = self.b1.id

    def tearDown(self):
        """Tear down test methods"""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_update(self):
        """Test for update"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual("** class name missing **", f.getvalue().strip())

    def test_update_with_class(self):
        """Test for update with class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel"))
            self.assertEqual("** instance id missing **", f.getvalue().strip())

    def test_update_with_class_id(self):
        """Test for update with class id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel {}"
                                                  .format(self.b1_id)))
            self.assertEqual("** attribute name missing **",
                             f.getvalue().strip())

    def test_update_with_class_id_attr(self):
        """Test for update with class id attr"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel {} name".
                                                  format(self.b1_id)))
            self.assertEqual("** value missing **", f.getvalue().strip())

    def test_update_with_class_id_attr_value(self):
        """Test for update with class id attr value"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel {} "
                                                  "name Me".
                                                  format(self.b1_id)))
            self.assertEqual("", f.getvalue().strip())

    def test_update_with_class_id_attr_value_invalid(self):
        """Test for update with class id attr value invalid"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel {} "
                                                  "email Mr".
                                                  format(self.b1_id)))
            self.assertEqual("", f.getvalue().strip())

    def test_update_with_class_id_attr_value_invalid(self):
        """Test for update with class id attr value invalid"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel {} "
                                                  "email Re".
                                                  format(self.b1_id)))
            self.assertEqual("", f.getvalue().strip())
