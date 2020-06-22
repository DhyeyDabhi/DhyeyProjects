from unittest.mock import patch
import unittest

import code

#Contains 8 tests as following:
#1) test_all_availaibe          i.e testing all available mode
#2) test_least_busy             i.e testing least busy mode
#3) test_random                 i.e testing random mode
#4) test_int_errors             i.e testing non integer error where integers accepted
#5) test_n_insteadof_y          i.e testing available_since works if 'n' is given input instead of 'y'
#6) test_less_agents_mass_issue i.e testing less agents input and more issues argument
#7) test_mass_agents_less_issue i.e testing mass agent input and less issues argument
#8) test_mass_agents_mass_issue i.e testing mass agent input and mass issues argument
class CodeTestCase(unittest.TestCase):

    def test_all_availaibe(self):
        user_input=[
        '2',
        'spanish',
        'english',
        '3',
        'Dhyey',
        'y',
        '145',
        'spanish',
        'Navin',
        'y',
        '100',
        'spanish speaker',
        'Varun',
        'y',
        '200',
        'english',
        'All Available',
        'All Available'
        ]

        user_function_input=[
        '3',
        'Dhyey',
        'y',
        '145',
        'spanish',
        'Navin',
        'y',
        '100',
        'spanish speaker',
        'Varun',
        'y',
        '200',
        'english',
        'All Available',
        'All Available'
        ]

        issue_lst=['spanish', 'english']
        with patch('builtins.input',side_effect=user_function_input ):
             output0=code.agent_selector_main(issue_lst)
        self.assertEqual(output0,[['Dhyey', 'Navin'],['Varun']])

        with patch('builtins.input',side_effect=user_input ):
            output=code.main()
        self.assertEqual(output,"All Agent Selections for given Issues done.")

    def test_least_busy(self):
        user_input=[
        '2',
        'spanish',
        'english',
        '3',
        'Dhyey',
        'y',
        '145',
        'spanish',
        'Navin',
        'y',
        '100',
        'spanish speaker',
        'Varun',
        'y',
        '200',
        'english',
        'Least Busy',
        'Least Busy'
        ]

        user_function_input=[
        '3',
        'Dhyey',
        'y',
        '145',
        'spanish',
        'Navin',
        'y',
        '100',
        'spanish speaker',
        'Varun',
        'y',
        '200',
        'english',
        'Least Busy',
        'Least Busy'
        ]

        issue_lst=['spanish', 'english']

        with patch('builtins.input',side_effect=user_function_input ):
             output0=code.agent_selector_main(issue_lst)
        self.assertEqual(output0,[['Dhyey'],['Varun']])

        with patch('builtins.input',side_effect=user_input ):
            output=code.main()
        self.assertEqual(output,"All Agent Selections for given Issues done.")

    def test_random(self):
        user_input=[
        '2',
        'spanish',
        'english',
        '3',
        'Dhyey',
        'y',
        '145',
        'spanish',
        'Navin',
        'y',
        '100',
        'spanish speaker',
        'Varun',
        'y',
        '200',
        'english',
        'Random',
        'Random'
        ]

        user_function_input=[
        '3',
        'Dhyey',
        'y',
        '145',
        'spanish',
        'Navin',
        'y',
        '100',
        'spanish speaker',
        'Varun',
        'y',
        '200',
        'english',
        'Random',
        'Random'
        ]

        issue_lst=['spanish', 'english']

        with patch('builtins.input',side_effect=user_function_input ):
             output0=code.agent_selector_main(issue_lst)
        try:
            self.assertEqual(output0,[['Dhyey'],['Varun']])
        except:
            self.assertEqual(output0,[['Navin'],['Varun']])

        with patch('builtins.input',side_effect=user_input ):
            output=code.main()
        self.assertEqual(output,"All Agent Selections for given Issues done.")

    def test_int_errors(self):
        user_input=[
        '2ww',
        'ww',
        '2',
        'spanish',
        'english',
        'wee3',
        'dsd',
        '3',
        'Dhyey',
        'y',
        '145',
        'spanish',
        'Navin',
        'y',
        'wer',
        '100',
        'spanish speaker',
        'Varun',
        'y',
        '200',
        'english',
        'All Available',
        'All Available'
        ]

        user_function_input=[
        'wee3',
        'dsd',
        '3',
        'Dhyey',
        'y',
        '145',
        'spanish',
        'Navin',
        'y',
        'wer',
        '100',
        'spanish speaker',
        'Varun',
        'y',
        '200',
        'english',
        'All Available',
        'All Available'
        ]

        issue_lst=['spanish', 'english']
        with patch('builtins.input',side_effect=user_function_input ):
             output0=code.agent_selector_main(issue_lst)
        self.assertEqual(output0,[['Dhyey', 'Navin'],['Varun']])

        with patch('builtins.input',side_effect=user_input ):
            output=code.main()
        self.assertEqual(output,"All Agent Selections for given Issues done.")

    def test_n_insteadof_y(self):
        user_input=[
        '2',
        'spanish',
        'english',
        '3',
        'Dhyey',
        'n',
        'spanish',
        'Navin',
        'y',
        '100',
        'spanish speaker',
        'Varun',
        'n',
        'english',
        'Random',
        'Random'
        ]

        user_function_input=[
        '3',
        'Dhyey',
        'n',
        'spanish',
        'Navin',
        'y',
        '100',
        'spanish speaker',
        'Varun',
        'n',
        'english',
        'Random',
        'Random'
        ]

        issue_lst=['spanish', 'english']

        with patch('builtins.input',side_effect=user_function_input ):
             output0=code.agent_selector_main(issue_lst)
        self.assertEqual(output0,[['Navin'],"No agents available."])

        with patch('builtins.input',side_effect=user_input ):
            output=code.main()
        self.assertEqual(output,"All Agent Selections for given Issues done.")

    def test_mass_agents_less_issue(self):
        def test_all_availaibe(self):
            user_input=[
            '2',
            'spanish',
            'english',
            '6',
            'Dhyey',
            'y',
            '145',
            'spanish',
            'Navin',
            'y',
            '100',
            'spanish speaker',
            'Varun',
            'y',
            '200',
            'english',
            'Dev',
            'n',
            'english',
            'Ukshit',
            'y',
            '55',
            'spanish',
            'Stanley',
            'n',
            'english'
            'All Available',
            'All Available'
            ]

            user_function_input=[
            '6',
            'Dhyey',
            'y',
            '145',
            'spanish',
            'Navin',
            'y',
            '100',
            'spanish speaker',
            'Varun',
            'y',
            '200',
            'english',
            'Dev',
            'n',
            'english',
            'Ukshit',
            'y',
            '55',
            'spanish',
            'Stanley',
            'n',
            'english'
            'All Available',
            'All Available'
            ]

            issue_lst=['spanish', 'english']
            with patch('builtins.input',side_effect=user_function_input ):
                 output0=code.agent_selector_main(issue_lst)
            self.assertEqual(output0,[['Dhyey', 'Navin','Ukshit'],['Varun']])

            with patch('builtins.input',side_effect=user_input ):
                output=code.main()
            self.assertEqual(output,"All Agent Selections for given Issues done.")

    def test_less_agents_mass_issue(self):
        user_input=[
        '6',
        'spanish',
        'english',
        'english',
        'english',
        'Hindi',
        'Gujarati',
        '3',
        'Dhyey',
        'y',
        '145',
        'spanish',
        'Navin',
        'y',
        '100',
        'spanish speaker',
        'Varun',
        'y',
        '200',
        'english',
        'All Available',
        'Least Busy',
        'Random',
        'All Available',
        'Least Busy',
        'All Available'
        ]

        user_function_input=[
        '3',
        'Dhyey',
        'y',
        '145',
        'spanish',
        'Navin',
        'y',
        '100',
        'spanish speaker',
        'Varun',
        'y',
        '200',
        'english',
        'All Available',
        'Least Busy',
        'Random',
        'All Available',
        'Least Busy',
        'All Available'
        ]

        issue_lst=['spanish', 'english','english','english','Hindi','Gujarati']
        with patch('builtins.input',side_effect=user_function_input ):
             output0=code.agent_selector_main(issue_lst)
        self.assertEqual(output0,[['Dhyey', 'Navin'],['Varun'],['Varun'],['Varun'],"No agents available.","No agents available."])

        with patch('builtins.input',side_effect=user_input ):
            output=code.main()
        self.assertEqual(output,"All Agent Selections for given Issues done.")

    def test_mass_agents_mass_issue(self):
        user_input=[
        '6',
        'spanish',
        'english',
        'english',
        'english',
        'Hindi',
        'Gujarati',
        '6',
        'Dhyey',
        'y',
        '145',
        'spanish',
        'Navin',
        'y',
        '100',
        'spanish speaker',
        'Varun',
        'y',
        '200',
        'english',
        'Dev',
        'n',
        'Gujarati',
        'Ukshit',
        'y',
        '55',
        'Hindi',
        'Stanley',
        'n',
        'english',
        'All Available',
        'Least Busy',
        'Random',
        'All Available',
        'Least Busy',
        'All Available'
        ]

        user_function_input=[
        '6',
        'Dhyey',
        'y',
        '145',
        'spanish',
        'Navin',
        'y',
        '100',
        'spanish speaker',
        'Varun',
        'y',
        '200',
        'english',
        'Dev',
        'n',
        'Gujarati',
        'Ukshit',
        'y',
        '55',
        'Hindi',
        'Stanley',
        'n',
        'english',
        'All Available',
        'Least Busy',
        'Random',
        'All Available',
        'Least Busy',
        'All Available'
        ]

        issue_lst=['spanish', 'english','english','english','Hindi','Gujarati']
        with patch('builtins.input',side_effect=user_function_input ):
             output0=code.agent_selector_main(issue_lst)
        self.assertEqual(output0,[['Dhyey', 'Navin'],['Varun'],['Varun'],['Varun'],['Ukshit'],"No agents available."])

        with patch('builtins.input',side_effect=user_input ):
            output=code.main()
        self.assertEqual(output,"All Agent Selections for given Issues done.")

if __name__ == '__main__':
    unittest.main()
