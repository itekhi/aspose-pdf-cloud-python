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


class Page(object):
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
        'links': 'list[Link]',
        'id': 'int',
        'images': 'Images',
        'rectangle': 'Rectangle'
    }

    attribute_map = {
        'links': 'Links',
        'id': 'Id',
        'images': 'Images',
        'rectangle': 'Rectangle'
    }

    def __init__(self, links=None, id=None, images=None, rectangle=None):
        """
        Page - a model defined in Swagger
        """

        self._links = None
        self._id = None
        self._images = None
        self._rectangle = None

        if links is not None:
          self.links = links
        if id is not None:
          self.id = id
        if images is not None:
          self.images = images
        if rectangle is not None:
          self.rectangle = rectangle

    @property
    def links(self):
        """
        Gets the links of this Page.
        Link to the document.

        :return: The links of this Page.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this Page.
        Link to the document.

        :param links: The links of this Page.
        :type: list[Link]
        """

        self._links = links

    @property
    def id(self):
        """
        Gets the id of this Page.
        Page's id.

        :return: The id of this Page.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Page.
        Page's id.

        :param id: The id of this Page.
        :type: int
        """

        self._id = id

    @property
    def images(self):
        """
        Gets the images of this Page.

        :return: The images of this Page.
        :rtype: Images
        """
        return self._images

    @images.setter
    def images(self, images):
        """
        Sets the images of this Page.

        :param images: The images of this Page.
        :type: Images
        """

        self._images = images

    @property
    def rectangle(self):
        """
        Gets the rectangle of this Page.

        :return: The rectangle of this Page.
        :rtype: Rectangle
        """
        return self._rectangle

    @rectangle.setter
    def rectangle(self, rectangle):
        """
        Sets the rectangle of this Page.

        :param rectangle: The rectangle of this Page.
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
        if not isinstance(other, Page):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
