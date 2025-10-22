from dataclasses import dataclass

@dataclass
class UserInfo:
    cif_no: str
    phone: str
    nid: str
    name: str

    @staticmethod
    def from_dict(obj):
        _cif_no = str(obj.get("cif_no", ""))
        _phone = str(obj.get("phone", ""))
        _nid = str(obj.get("nid"))
        _name = str(obj.get("name"))

        return UserInfo(
            _cif_no,
            _phone,
            _nid,
            _name,
        )
    

user_data = {
    "cif_no": "112345",
    "phone": "01942831359",
    "nid": "23454545",
    "name": "rayhan"
}

user_info = UserInfo.from_dict(user_data)

print(user_info.cif_no)

print(user_info)
