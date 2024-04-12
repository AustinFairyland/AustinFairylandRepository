# coding: utf8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 02 29, 2024
"""
import sys
import warnings
import threading
from concurrent.futures import ThreadPoolExecutor
from deprecated import deprecated

from fairyland.framework.modules.journals.Journal import journal, logger
from fairyland.framework.core.abstracts.enumerate.Enumerate import BaseEnum, StringEnum, IntegerEnum
from fairyland.framework.constants.enum import DateTimeFormat
from fairyland.framework.modules.exceptions import ProgramError
from fairyland.framework.utils.generals.constants.Constants import DefaultConstantUtils
from fairyland.framework.utils.generals.datetime.DateTime import DatetimeUtils
from fairyland.framework.utils.publish.package import PackageInfo
from fairyland.framework.utils.generals.decoder.Decoder import DecoderUtils
from fairyland.framework.utils.generals.constants.Constants import EncodingConstantUtils
from fairyland.framework.modules.decorators.patterns.Design import SingletonPattern
from fairyland.framework.core.abstracts.metaclass.MetaClass import SingletonPatternMetaclass
from fairyland.framework.modules.decorators.methods.Method import MethodActionDecorator
from fairyland.framework.modules.decorators.methods.Method import MethodTimingDecorator
from fairyland.framework.modules.datasource.Mysql import MySQLModule
from fairyland.framework.modules.static.requests.Requests import Requests
from fairyland.framework.utils.tools.requests import RequestsUtils
from fairyland.framework.modules.decorators.methods.Method import MethodTryCatchDecorator, MethodTipsDecorator
from fairyland.framework.utils.tools import VariableTools

from fairyland.framework.test.simulation import TestReturn

sys.dont_write_bytecode = True
warnings.filterwarnings("ignore")


@SingletonPattern
class A: ...


class B(metaclass=SingletonPatternMetaclass): ...


class TestEnum(IntegerEnum):
    a = 12138


class TestBase:
    _version = "1.0.0"


class TestVersion(TestBase):

    def __init__(self):
        self.version = self._version


def thread_test():
    def inner_1(total, _tips):
        for index in range(total):
            print(f"Inner 1 | {_tips}: {index}")

    a = threading.Thread(target=inner_1, args=(20, "Thread 1"))
    b = threading.Thread(target=inner_1, args=(10, "Thread 2"))

    a.start()
    b.start()

    print("Done")


class Test:

    @classmethod
    # @logger.catch()
    @MethodTimingDecorator
    # @MethodActionDecorator("Test Main Method.")
    def run(cls) -> None:
        cls.test_1()
        cls.test_2()
        cls.test_3()
        cls.test_4()
        cls.test_5()
        cls.test_6()
        cls.test_7()
        cls.test_8()
        cls.test_9()
        cls.test_10()
        cls.test_11()
        cls.test_12()
        cls.test_13()
        cls.test_14()
        cls.test_15()
        cls.test_16(10, "1")
        cls.test_17()
        cls.test_18()
        cls.test_19()
        cls.test_20()
        cls.test_21()
        cls.test_22()
        cls.test_23()
        cls.test_24()
        cls.test_25()
        cls.test_26()

    @classmethod
    @MethodActionDecorator("Test 1")
    def test_1(cls):
        class DatetimeEnum(BaseEnum):
            data = {"a": 1}

        journal.debug(f"测试枚举继承方法: {DatetimeEnum.values()}")

    @classmethod
    @MethodActionDecorator("Test 2")
    def test_2(cls):
        journal.debug(f"日期时间格式化枚举成员: {DateTimeFormat.members()}")
        journal.debug(f"日期时间格式化枚举字段: {DateTimeFormat.names()}")
        journal.debug(f"日期时间格式化枚举值: {DateTimeFormat.values()}")
        journal.debug(f"日期时间格式化: {DateTimeFormat.datetime_cn.value}")

    @classmethod
    @MethodActionDecorator("Test 3")
    def test_3(cls):
        journal.debug(f"当前时间时间戳: {DatetimeUtils.normtimestamp()}")
        a = DefaultConstantUtils.dict()
        a.update(测试时间=DatetimeUtils.normdatetime_to_string())
        journal.debug(f"测试字典: {a}")

    @classmethod
    @MethodActionDecorator("Test 4")
    def test_4(cls):
        journal.debug(f"包名: {PackageInfo.name}")
        journal.debug(f"版本号: {PackageInfo.version}")

    @classmethod
    @MethodActionDecorator("Test 5")
    def test_5(cls):
        b_str = b"\xd3\xd0\xb9\xd8\xc4\xb3\xb8\xf6\xc3\xfc\xc1\xee\xb5\xc4\xcf\xea\xcf\xb8\xd0\xc5\xcf\xa2\xa3\xac\xc7\xeb\xbc\xfc\xc8\xeb HELP \xc3\xfc\xc1\xee\xc3\xfb\r\nASSOC"
        a = DecoderUtils.decode_binary_string(b_str, encodings=EncodingConstantUtils.encodings())
        journal.debug(f"解码: {a}")

    @classmethod
    @MethodActionDecorator("Test 6")
    def test_6(cls):
        string = "big5, big5-hkscs, cesu-8, euc-jp, euc-kr, gb18030, gb2312, gbk, ibm-thai, ibm00858, ibm01140, ibm01141, ibm01142, ibm01143, ibm01144, ibm01145, ibm01146, ibm01147, ibm01148, ibm01149, ibm037, ibm1026, ibm1047, ibm273, ibm277, ibm278, ibm280, ibm284, ibm285, ibm290, ibm297, ibm420, ibm424, ibm437, ibm500, ibm775, ibm850, ibm852, ibm855, ibm857, ibm860, ibm861, ibm862, ibm863, ibm864, ibm865, ibm866, ibm868, ibm869, ibm870, ibm871, ibm918, iso-2022-cn, iso-2022-jp, iso-2022-jp-2, iso-2022-kr, iso-8859-1, iso-8859-13, iso-8859-15, iso-8859-2, iso-8859-3, iso-8859-4, iso-8859-5, iso-8859-6, iso-8859-7, iso-8859-8, iso-8859-9, jis_x0201, jis_x0212-1990, koi8-r, koi8-u, shift_jis, tis-620, us-ascii, utf-16, utf-16be, utf-16le, utf-32, utf-32be, utf-32le, utf-8, windows-1250, windows-1251, windows-1252, windows-1253, windows-1254, windows-1255, windows-1256, windows-1257, windows-1258, windows-31j, x-big5-hkscs-2001, x-big5-solaris, x-euc-jp-linux, x-euc-tw, x-eucjp-open, x-ibm1006, x-ibm1025, x-ibm1046, x-ibm1097, x-ibm1098, x-ibm1112, x-ibm1122, x-ibm1123, x-ibm1124, x-ibm1166, x-ibm1364, x-ibm1381, x-ibm1383, x-ibm300, x-ibm33722, x-ibm737, x-ibm833, x-ibm834, x-ibm856, x-ibm874, x-ibm875, x-ibm921, x-ibm922, x-ibm930, x-ibm933, x-ibm935, x-ibm937, x-ibm939, x-ibm942, x-ibm942c, x-ibm943, x-ibm943c, x-ibm948, x-ibm949, x-ibm949c, x-ibm950, x-ibm964, x-ibm970, x-iscii91, x-iso-2022-cn-cns, x-iso-2022-cn-gb, x-iso-8859-11, x-jis0208, x-jisautodetect, x-johab, x-macarabic, x-maccentraleurope, x-maccroatian, x-maccyrillic, x-macdingbat, x-macgreek, x-machebrew, x-maciceland, x-macroman, x-macromania, x-macsymbol, x-macthai, x-macturkish, x-macukraine, x-ms932_0213, x-ms950-hkscs, x-ms950-hkscs-xp, x-mswin-936, x-pck, x-sjis_0213, x-utf-16le-bom, x-utf-32be-bom, x-utf-32le-bom, x-windows-50220, x-windows-50221, x-windows-874, x-windows-949, x-windows-950, x-windows-iso2022jp"
        string_tuple = tuple([item for item in string.replace(" ", "").split(",")])
        journal.debug(f"字符集: {string_tuple}")
        journal.debug(f"字符集数量: {string_tuple.__len__()}")

    @classmethod
    @MethodActionDecorator("Test 7")
    def test_7(cls):
        a = A()
        aa = A()
        if a == aa:
            journal.debug(True)
        else:
            journal.debug(False)

    @classmethod
    @MethodActionDecorator("Test 8")
    def test_8(cls):
        b = B()
        bb = B()
        if b == bb:
            journal.debug(True)
        else:
            journal.debug(False)

    @classmethod
    @MethodActionDecorator("Test 9")
    def test_9(cls):
        db = MySQLModule(host="mapping.fairy.host", port=51001, user="austin", password="Austin.pwd:112#.", database="public_db_test")
        query_tuple = ("select version();", "select * from myapp_myinfo where nid > %s;")
        param_tuple = (None, 0)
        a = db.operate(query_tuple, param_tuple)
        journal.debug(a)

    @classmethod
    @MethodActionDecorator("Test 10")
    def test_10(cls):
        response = Requests.get(
            url="https://api.threatbook.cn/v3/scene/ip_reputation",
            params={"apikey": "25702dcf45db4f4c95dac98cabe0b6f9", "resource": "159.203.93.255"},
        )
        journal.debug(f"Response: {response}")
        journal.debug(f"Type: {type(response)}")

    @classmethod
    @MethodActionDecorator("Test 11")
    def test_11(cls):
        journal.debug(f"当前时间戳: {DatetimeUtils.normtimestamp()}")
        # 1709636127
        # journal.debug(f"{DatetimeUtils.timestamp_to_datetime(1709626679000)}")
        # journal.debug(f"{DatetimeUtils.timestamp_to_datetime(1709636127)}")
        journal.debug(f"{DatetimeUtils.timestamp_to_datetime(1709892785)}")
        journal.debug(f"{DatetimeUtils.timestamp_to_datetime(1709892786)}")

    @classmethod
    @MethodActionDecorator("Test 12")
    def test_12(cls):
        journal.debug(f"{RequestsUtils.user_agent()}, type: {type(RequestsUtils.user_agent())}")
        journal.debug(f"{RequestsUtils.chrome_user_agent()}")
        journal.debug(f"{RequestsUtils.edge_user_agent()}")
        journal.debug(f"{RequestsUtils.firefox_user_agent()}")
        journal.debug(f"{RequestsUtils.safari_user_agent()}")

    @classmethod
    @MethodActionDecorator("Test 13")
    def test_13(cls):
        # a = Requests.get("https://baidu.com")
        b = Requests.get("https://douban.api.fairy.host")
        # b = Requests.get("https://ttime.v1.timerecord.cn/asdqwefac")
        # journal.debug(f"Type a: {type(a)}")
        journal.debug(f"b: {b}, Type b: {type(b)}")
        if isinstance(b, dict):
            journal.debug(f"b -> code: {b.get('code')}")

    @classmethod
    @MethodActionDecorator("Test 14")
    def test_14(cls):
        for i in range(100, 3662, 100):
            journal.debug(i)
            break

    @classmethod
    @MethodActionDecorator("Test 15")
    def test_15(cls):
        logger.debug("If you're using Python {}, prefer {feature} of course!", 3.9, feature="f-strings")
        journal.debug("If you're using Python {}, prefer {feature} of course!", 3.9, feature="f-strings")
        logger.opt(lazy=True).debug("If you're using Python {}, prefer {feature} of course!")

    @classmethod
    @MethodActionDecorator("Test 16")
    def test_16(cls, total, msg):

        def inner_1(total, _tips):
            for index in range(total):
                # journal.debug(f"Inner 1 | {_tips}: {index}")
                print(f"Inner 1 | {_tips}: {index}")

        for index in range(total):
            journal.debug(f"Test 16 -> {msg} : {index}")

        # a = threading.Thread(target=inner_1, args=(20, "Thread 1"))
        # b = threading.Thread(target=inner_1, args=(10, "Thread 2"))

        # a.start()
        # b.start()

        # journal.success("Done")

    @classmethod
    def get_thread_pool(cls) -> ThreadPoolExecutor:
        return ThreadPoolExecutor(max_workers=10)

    @classmethod
    @MethodTimingDecorator
    @MethodActionDecorator("Test 17")
    def test_17(cls):
        def inner(total=10):
            a = 0
            for i in range(total):
                a += i

            return a

        thread_pool = cls.get_thread_pool()
        results = thread_pool.submit(inner).result()
        # results = inner()
        thread_pool.shutdown()
        journal.debug(f"Results = {results}")

    @classmethod
    @MethodActionDecorator("Test 18")
    def test_18(cls):
        a = TestEnum.get("a")
        journal.debug(f"Test Enum: {a}, Type: {type(a)}")

    @classmethod
    @MethodActionDecorator("Test 19")
    def test_19(cls):
        start_time, end_time = 1709892785, 1709892786
        if start_time.__str__().__len__() < 13:
            start_time = int(start_time.__str__().ljust(13, "0"))
        if end_time.__str__().__len__() < 13:
            end_time = int(end_time.__str__().ljust(13, "0"))
        journal.debug(f"Start Time: {start_time}, End Time: {end_time}")
        journal.debug(f"Start Time Type: {type(start_time)}, End Time Type: {type(end_time)}")

    @classmethod
    @MethodTimingDecorator
    @MethodActionDecorator("Test 20")
    # @MethodTryCatchDecorator
    def test_20(cls):
        # try:
        aa = (1, 2, 3)
        journal.debug(aa.__getitem__(0))
        journal.debug(aa.__getitem__(1))
        journal.debug(aa.__getitem__(2))
        journal.debug(aa.__getitem__(slice(0, 2)))

        try:
            a = 2 / 0
            journal.debug(a)
        except ZeroDivisionError as error:
            journal.error(error)

        # except Exception as error:
        #     journal.warning(error)

    @classmethod
    # @MethodTimingDecorator
    # @MethodActionDecorator(name="测试12")
    @MethodTryCatchDecorator
    @MethodTipsDecorator
    def test_21(cls):
        a: str = TestEnum.get("a")
        journal.debug(f"a -> {a}, type a -> {type(a)}")
        aa = TestEnum.a
        journal.debug(f"aa -> {aa}, type aa -> {type(aa)}")
        aaa = TestEnum.members()
        journal.debug(f"aaa -> {aaa}, type aaa -> {type(aaa)}")
        journal.debug(f"element 1 -> {aaa.__getitem__(0)}, element 1 type -> {type(aaa.__getitem__(0))}")

    @classmethod
    @MethodTryCatchDecorator
    @MethodTipsDecorator
    def test_22(cls):
        a = (1, 2, 3)
        for v in a:
            if v not in [3, 4, 5]:
                journal.debug(f"Not in: {v}")

    @classmethod
    @MethodTryCatchDecorator
    @MethodTipsDecorator
    def test_23(cls):
        journal.debug(ord("a"))
        a = [v for v in range(1, 11)]
        journal.debug(a.__getitem__(slice(None, None, 2)))
        a = [[1, 2]]
        ((a_1, _),) = a
        journal.debug((a_1,))

    @classmethod
    @MethodTryCatchDecorator
    @MethodTipsDecorator
    def test_24(cls):
        journal.debug(tuple(i for i in range(1, 11)))
        journal.debug(tuple([i for i in range(1, 11)]))
        aa = (1, 2, 3)
        journal.debug(tuple(filter(lambda x: x not in aa, range(0, 6))))
        if TestEnum.a == 12138:
            journal.debug("Yes")
        journal.debug((TestEnum.a.value, type(TestEnum.a.value)))

    @classmethod
    @deprecated(reason="Deprecated Method")
    def test_25(cls):
        journal.debug("Deprecated Method")

    @classmethod
    @MethodActionDecorator(name="test 26")
    def test_26(cls):
        a = 123123
        journal.debug(VariableTools.get_var_name(a, locals()))


if __name__ == "__main__":
    # Test.run()
    Test.test_26()
