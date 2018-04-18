# coding: utf-8

"""
    Aspose.PDF for Cloud API Reference


   Copyright (c) 2018 Aspose.Pdf for Cloud
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



    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Paragraph(object):
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
        'line_spacing': 'LineSpacing',
        'wrap_mode': 'WrapMode',
        'horizontal_alignment': 'TextHorizontalAlignment',
        'left_margin': 'float',
        'right_margin': 'float',
        'top_margin': 'float',
        'bottom_margin': 'float',
        'rectangle': 'Rectangle',
        'rotation': 'float',
        'subsequent_lines_indent': 'float',
        'vertical_alignment': 'VerticalAlignment',
        'lines': 'list[TextLine]'
    }

    attribute_map = {
        'line_spacing': 'LineSpacing',
        'wrap_mode': 'WrapMode',
        'horizontal_alignment': 'HorizontalAlignment',
        'left_margin': 'LeftMargin',
        'right_margin': 'RightMargin',
        'top_margin': 'TopMargin',
        'bottom_margin': 'BottomMargin',
        'rectangle': 'Rectangle',
        'rotation': 'Rotation',
        'subsequent_lines_indent': 'SubsequentLinesIndent',
        'vertical_alignment': 'VerticalAlignment',
        'lines': 'Lines'
    }

    def __init__(self, line_spacing=None, wrap_mode=None, horizontal_alignment=None, left_margin=None, right_margin=None, top_margin=None, bottom_margin=None, rectangle=None, rotation=None, subsequent_lines_indent=None, vertical_alignment=None, lines=None):
        """
        Paragraph - a model defined in Swagger
        """

        self._line_spacing = None
        self._wrap_mode = None
        self._horizontal_alignment = None
        self._left_margin = None
        self._right_margin = None
        self._top_margin = None
        self._bottom_margin = None
        self._rectangle = None
        self._rotation = None
        self._subsequent_lines_indent = None
        self._vertical_alignment = None
        self._lines = None

        if line_spacing is not None:
          self.line_spacing = line_spacing
        if wrap_mode is not None:
          self.wrap_mode = wrap_mode
        if horizontal_alignment is not None:
          self.horizontal_alignment = horizontal_alignment
        if left_margin is not None:
          self.left_margin = left_margin
        if right_margin is not None:
          self.right_margin = right_margin
        if top_margin is not None:
          self.top_margin = top_margin
        if bottom_margin is not None:
          self.bottom_margin = bottom_margin
        if rectangle is not None:
          self.rectangle = rectangle
        if rotation is not None:
          self.rotation = rotation
        if subsequent_lines_indent is not None:
          self.subsequent_lines_indent = subsequent_lines_indent
        if vertical_alignment is not None:
          self.vertical_alignment = vertical_alignment
        self.lines = lines

    @property
    def line_spacing(self):
        """
        Gets the line_spacing of this Paragraph.

        :return: The line_spacing of this Paragraph.
        :rtype: LineSpacing
        """
        return self._line_spacing

    @line_spacing.setter
    def line_spacing(self, line_spacing):
        """
        Sets the line_spacing of this Paragraph.

        :param line_spacing: The line_spacing of this Paragraph.
        :type: LineSpacing
        """

        self._line_spacing = line_spacing

    @property
    def wrap_mode(self):
        """
        Gets the wrap_mode of this Paragraph.

        :return: The wrap_mode of this Paragraph.
        :rtype: WrapMode
        """
        return self._wrap_mode

    @wrap_mode.setter
    def wrap_mode(self, wrap_mode):
        """
        Sets the wrap_mode of this Paragraph.

        :param wrap_mode: The wrap_mode of this Paragraph.
        :type: WrapMode
        """

        self._wrap_mode = wrap_mode

    @property
    def horizontal_alignment(self):
        """
        Gets the horizontal_alignment of this Paragraph.

        :return: The horizontal_alignment of this Paragraph.
        :rtype: TextHorizontalAlignment
        """
        return self._horizontal_alignment

    @horizontal_alignment.setter
    def horizontal_alignment(self, horizontal_alignment):
        """
        Sets the horizontal_alignment of this Paragraph.

        :param horizontal_alignment: The horizontal_alignment of this Paragraph.
        :type: TextHorizontalAlignment
        """

        self._horizontal_alignment = horizontal_alignment

    @property
    def left_margin(self):
        """
        Gets the left_margin of this Paragraph.

        :return: The left_margin of this Paragraph.
        :rtype: float
        """
        return self._left_margin

    @left_margin.setter
    def left_margin(self, left_margin):
        """
        Sets the left_margin of this Paragraph.

        :param left_margin: The left_margin of this Paragraph.
        :type: float
        """

        self._left_margin = left_margin

    @property
    def right_margin(self):
        """
        Gets the right_margin of this Paragraph.

        :return: The right_margin of this Paragraph.
        :rtype: float
        """
        return self._right_margin

    @right_margin.setter
    def right_margin(self, right_margin):
        """
        Sets the right_margin of this Paragraph.

        :param right_margin: The right_margin of this Paragraph.
        :type: float
        """

        self._right_margin = right_margin

    @property
    def top_margin(self):
        """
        Gets the top_margin of this Paragraph.

        :return: The top_margin of this Paragraph.
        :rtype: float
        """
        return self._top_margin

    @top_margin.setter
    def top_margin(self, top_margin):
        """
        Sets the top_margin of this Paragraph.

        :param top_margin: The top_margin of this Paragraph.
        :type: float
        """

        self._top_margin = top_margin

    @property
    def bottom_margin(self):
        """
        Gets the bottom_margin of this Paragraph.

        :return: The bottom_margin of this Paragraph.
        :rtype: float
        """
        return self._bottom_margin

    @bottom_margin.setter
    def bottom_margin(self, bottom_margin):
        """
        Sets the bottom_margin of this Paragraph.

        :param bottom_margin: The bottom_margin of this Paragraph.
        :type: float
        """

        self._bottom_margin = bottom_margin

    @property
    def rectangle(self):
        """
        Gets the rectangle of this Paragraph.

        :return: The rectangle of this Paragraph.
        :rtype: Rectangle
        """
        return self._rectangle

    @rectangle.setter
    def rectangle(self, rectangle):
        """
        Sets the rectangle of this Paragraph.

        :param rectangle: The rectangle of this Paragraph.
        :type: Rectangle
        """

        self._rectangle = rectangle

    @property
    def rotation(self):
        """
        Gets the rotation of this Paragraph.

        :return: The rotation of this Paragraph.
        :rtype: float
        """
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        """
        Sets the rotation of this Paragraph.

        :param rotation: The rotation of this Paragraph.
        :type: float
        """

        self._rotation = rotation

    @property
    def subsequent_lines_indent(self):
        """
        Gets the subsequent_lines_indent of this Paragraph.

        :return: The subsequent_lines_indent of this Paragraph.
        :rtype: float
        """
        return self._subsequent_lines_indent

    @subsequent_lines_indent.setter
    def subsequent_lines_indent(self, subsequent_lines_indent):
        """
        Sets the subsequent_lines_indent of this Paragraph.

        :param subsequent_lines_indent: The subsequent_lines_indent of this Paragraph.
        :type: float
        """

        self._subsequent_lines_indent = subsequent_lines_indent

    @property
    def vertical_alignment(self):
        """
        Gets the vertical_alignment of this Paragraph.

        :return: The vertical_alignment of this Paragraph.
        :rtype: VerticalAlignment
        """
        return self._vertical_alignment

    @vertical_alignment.setter
    def vertical_alignment(self, vertical_alignment):
        """
        Sets the vertical_alignment of this Paragraph.

        :param vertical_alignment: The vertical_alignment of this Paragraph.
        :type: VerticalAlignment
        """

        self._vertical_alignment = vertical_alignment

    @property
    def lines(self):
        """
        Gets the lines of this Paragraph.

        :return: The lines of this Paragraph.
        :rtype: list[TextLine]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """
        Sets the lines of this Paragraph.

        :param lines: The lines of this Paragraph.
        :type: list[TextLine]
        """
        if lines is None:
            raise ValueError("Invalid value for `lines`, must not be `None`")

        self._lines = lines

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
        if not isinstance(other, Paragraph):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
