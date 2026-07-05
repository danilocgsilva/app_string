class FileListConfig:
    _ignore_git: bool
    _ignore_node_modules: bool
    _ignore_vendor: bool
    _only_path: bool
    _ignore_var_cache: bool
    _full_path: bool

    def __init__(self):
        self._ignore_git = True
        self._ignore_node_modules = True
        self._ignore_vendor = True
        self._only_path = False
        self._ignore_var_cache = True
        self._full_path = True
        self._regex_ignore = ""

    @property
    def regex_ignore(self) -> str:
        return self._regex_ignore

    @regex_ignore.setter
    def regex_ignore(self, regex: str):
        self._regex_ignore = regex

    @property
    def full_path(self) -> bool:
        return self._full_path
    
    @full_path.setter
    def full_path(self, value: bool):
        self._full_path = value

    @property
    def ignore_var_cache(self) -> bool:
        return self._ignore_var_cache

    @ignore_var_cache.setter
    def ignore_var_cache(self, value: bool):
        self._ignore_var_cache = value

    @property
    def ignore_git(self) -> bool:
        return self._ignore_git

    @ignore_git.setter
    def ignore_git(self, value: bool):
        self._ignore_git = value

    @property
    def ignore_node_modules(self) -> bool:
        return self._ignore_node_modules

    @ignore_node_modules.setter
    def ignore_node_modules(self, value: bool):
        self._ignore_node_modules = value

    @property
    def ignore_vendor(self) -> bool:
        return self._ignore_vendor

    @ignore_vendor.setter
    def ignore_vendor(self, value: bool):
        self._ignore_vendor = value

    @property
    def only_path(self) -> bool:
        return self._only_path

    @only_path.setter
    def only_path(self, value: bool):
        self._only_path = value
    
