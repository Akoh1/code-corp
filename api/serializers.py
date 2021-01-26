from rest_framework import serializers, status
from .models import Profile, Tags, Question, Answers, AnsComment, QuesComment
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
import logging
from django.shortcuts import get_object_or_404
import datetime

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id' ,'username', 'first_name', 
                  'last_name', 'email',
                  'password')
        read_only_fields = ('id',)
        
        extra_kwargs = {
            "password": {"write_only": True},
            # 'username': {'required': False}
        }


class ProfileSerializer(serializers.ModelSerializer):
    """
    A student serializer to return the student details
    """
    user = UserSerializer(required=False)

    class Meta:
        model = Profile
        fields = ('id', 'uid', 'user', 'bio', 'location')
        read_only_fields = ('id', 'uid')
        # extra_kwargs = {
        #     "user": {'required': False},
        #     'question': {'required': False}
        # }
        # read_only_fields = ('user',)

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        user_data = validated_data.pop('user')
        # user = UserSerializer.create(UserSerializer(),
        #                              validated_data=user_data)
        user = User.objects.create(username=user_data['username'],
                                   first_name=user_data['first_name'],
                                   last_name=user_data['last_name'],
                                   email=user_data['email'],
                                   password=user_data['password'])

        profile, created = Profile.objects.update_or_create(user=user,
                            bio=validated_data.pop('bio'),
                            location=validated_data.pop('location'))
        return profile

    def update(self, instance, validated_data):
        print(validated_data)
        if 'user' in validated_data:
            user_data = validated_data.pop('user')
            user = instance.user
            user.username = user_data.get('username', user.username)
            user.first_name = user_data.get('first_name', user.first_name)
            user.last_name = user_data.get('last_name', user.last_name)

            user.save()

        instance.bio = validated_data.get('bio', instance.bio)
        instance.location = validated_data.get('location', 
                                               instance.location)
        instance.save()


        return instance


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['name',]
        # read_only_fields = ('id',)

    def create(self, validated_data):
        return Tags.objects.create(**validated_data)


class QuestionSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True)
    # tags = serializers.

    class Meta:
        model = Question
        fields = ['id', 'uid', 'user', 'title', 'question', 'tags', 
                  'date_created', 'updated']
        # read_only_fields = ('id',)
        # depth = 1
        # extra_kwargs = {
        #     "title": {'required': False},
        #     'question': {'required': False}
        # }

    def create(self, validated_data):
        tags_data =  validated_data.pop('tags')
        # print(tags_data)
        # tag = Tags.objects.filter(name__in=tags_data[0]['name'])
        # print(tag)
        users = validated_data.pop('user')
        # print(users)
        user = get_object_or_404(Profile, pk=users)
        # print(user)
        question = Question.objects.create(user=user,
                                           **validated_data)
        # question.tags.add(*tag)
        for tags in tags_data:
            # print(tags)
            tag = Tags.objects.filter(name=tags['name'])
            # print(tag)
            question.tags.add(*tag)
        return question

    def update(self, instance, validated_data):
        # tags_data = validated_data.pop('tags')
        # print(tags_data)
        # print("These are the tags")
        if 'tags' in validated_data:
            tags_data = validated_data.pop('tags')
            print("I am updating Question")
            print("These are the tags")
            print(tags_data)
            print(len(tags_data))
            test = Question.objects.get(pk=instance.id)
            print("Getting Question Objects")
            print(test.tags.all())
            qs = test.tags.all()
            tags_arr = []
            # for x in test.tags.all():
            #     tags_arr.append(x)
            #     print(x)
            
            for tags in tags_data:
                print("Update tags value")
                print(tags['name'])
                # d = dict(tags)
                # print("Convert to dict")
                # print(d)
                print("Counting")
                print(qs.count())
                print("check tags array")
                print(tags_arr)
                # for x in test.tags.all():
                #     print("Loop thru Question")
                #     print(x)
                #     if tags['name'] != x:
                #         print("Get not elem")
                #         print(x)
                # if tags['name'] in tags_arr:
                #     tags_arr.remove(tags['name'])
                #     for i in tags_arr:
                #         print("Check loop of tags array")
                #         print(i)
                #         get_tag = Tags.objects.get(name=i)
                #         instance.tags.remove(get_tag)

                # if qs.count() != len(tags_data):
                #     print("testing")
                #     instance.tags.exclude(name=tags['name']).remove()
                # tag = Tags.objects.get(name=tags['name'])
                tag = Tags.objects.filter(name=tags['name'])
                print(tag)
                instance.tags.add(*tag)
                # instance.tags.set(*tag)

        instance.updated = validated_data.get('updated',
                                              datetime.datetime.now())
        instance.title = validated_data.get('title', instance.title)
        instance.question = validated_data.get('question', 
                                               instance.question)
        instance.save()

        return instance


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answers
        fields = ['id', 'uid', 'user', 'question', 'text', 
                  'date_created', 'updated']

    def create(self, validated_data):
        users = validated_data.pop('user')
        user = get_object_or_404(Profile, pk=users)

        questions = validated_data.pop('question')
        question = get_object_or_404(Question, pk=questions)
        answer = Answers.objects.create(user=user,
                                        question=question,
                                        **validated_data)

        return answer

    def update(self, instance, validated_data):
        instance.updated = validated_data.get('updated',
                                              datetime.datetime.now())
        instance.text = validated_data.get('text', instance.text)
        return instance


class QuesCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuesComment
        fields = ['id', 'user', 'question', 'text', 
                  'date_created', 'updated']

    def create(self, validated_data):
        users = validated_data.pop('user')
        user = get_object_or_404(Profile, pk=users)

        questions = validated_data.pop('question')
        question = get_object_or_404(Question, pk=questions)
        comment = QuesComment.objects.create(user=user,
                                             question=question,
                                             **validated_data)

        return comment

    def update(self, instance, validated_data):
        instance.updated = validated_data.get('updated',
                                              datetime.datetime.now())
        instance.text = validated_data.get('text', instance.text)
        return instance


class AnsCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnsComment
        fields = ['id', 'user', 'answer', 'text', 
                  'date_created', 'updated']

    def create(self, validated_data):
        users = validated_data.pop('user')
        user = get_object_or_404(Profile, pk=users)

        answers = validated_data.pop('answer')
        answer = get_object_or_404(Answers, pk=answers)
        comment = AnsComment.objects.create(user=user,
                                            answer=answer,
                                            **validated_data)

        return comment

    def update(self, instance, validated_data):
        instance.updated = validated_data.get('updated',
                                              datetime.datetime.now())
        instance.text = validated_data.get('text', instance.text)
        return instance