# coding: utf-8

"""
    Aspose.PDF Cloud API Reference


   Copyright (c) 2019 Aspose.PDF Cloud
 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:
 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.



    OpenAPI spec version: 3.0
    
"""


from pprint import pformat
from six import iteritems
import re


class CellRecognized(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'text_rects': 'TextRects',
        'rectangle': 'Rectangle'
    }

    attribute_map = {
        'text_rects': 'TextRects',
        'rectangle': 'Rectangle'
    }

    def __init__(self, text_rects=None, rectangle=None):
        """
        CellRecognized - a model defined in Swagger
        """

        self._text_rects = None
        self._rectangle = None

        if text_rects is not None:
          self.text_rects = text_rects
        if rectangle is not None:
          self.rectangle = rectangle

    @property
    def text_rects(self):
        """
        Gets the text_rects of this CellRecognized.
        Gets collection of TextRect objects that describes text containing in the cell

        :return: The text_rects of this CellRecognized.
        :rtype: TextRects
        """
        return self._text_rects

    @text_rects.setter
    def text_rects(self, text_rects):
        """
        Sets the text_rects of this CellRecognized.
        Gets collection of TextRect objects that describes text containing in the cell

        :param text_rects: The text_rects of this CellRecognized.
        :type: TextRects
        """

        self._text_rects = text_rects

    @property
    def rectangle(self):
        """
        Gets the rectangle of this CellRecognized.
        Gets rectangle that describes position of the cell on page

        :return: The rectangle of this CellRecognized.
        :rtype: Rectangle
        """
        return self._rectangle

    @rectangle.setter
    def rectangle(self, rectangle):
        """
        Sets the rectangle of this CellRecognized.
        Gets rectangle that describes position of the cell on page

        :param rectangle: The rectangle of this CellRecognized.
        :type: Rectangle
        """

        self._rectangle = rectangle

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, CellRecognized):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
