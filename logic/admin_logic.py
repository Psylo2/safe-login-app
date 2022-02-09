from typing import Dict

from flask import flash

from usecases import AdminUseCase
from logic.services import AdminLogicService

from models.password.password import PasswordConfig
from models.user import User


class AdminLogic(AdminUseCase, AdminLogicService):
    def __init__(self):
        pass

    def users_list(self):
        all_users = User.find_all_from_db()
        return all_users

    def block_user(self, block) -> bool:
        for user in User.find_all_from_db():
            if len(list(set(block) & set(user._name))) == 0:
                user.block_user_model(block)
                return True
        return False

    def unblock_user(self, unblock) -> bool:
        for user in User.find_all_from_db():
            if len(list(set(unblock) & set(user._name))) == 0:
                user.unblock_user_model(unblock)
                return True
            return False

    def password_configuration(self, upper: bool, lower: bool, digits: bool,
                               spec: bool, use_dict: bool, length: str,
                               history: str, tries: str):

        configurations = self.extract_configuration_fields(upper=upper, lower=lower, digits=digits, spec=spec,
                                                           use_dict=use_dict, length=length, history=history,
                                                           tries=tries)
        result = PasswordConfig.set_config(**configurations)
        if result:
            flash('Password Configuration Changed!', 'danger')
            return True

        flash('Invalid Inputs', 'danger')
        return False

    def configure_regex(self, upper, lower, digits, spec) -> str:
        re = ""
        re += "A-Z" if upper else ""
        re += "a-z" if lower else ""
        re += "0-9" if digits else ""
        re += "\!\#\$\%\^\&\*\_\+\.\," if spec else ""
        return re

    def extract_configuration_fields(self, upper: bool, lower: bool, digits: bool,
                                     spec: bool, use_dict: bool, length: str,
                                     history: str, tries: str) -> Dict:
        regex = self.configure_regex(upper=upper, lower=lower, digits=digits, spec=spec)
        use_dict = True if use_dict == "1" else False
        return {
            "dictionary": use_dict,
            "regex": regex,
            "length": length,
            "history": history,
            "tries": tries
        }
