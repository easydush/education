import { apiClient } from './client';
import { AxiosResponse } from 'axios';
import { message } from 'antd';
import { setCourses, setCurrentCourse, setCurrentLesson, setMyCourses } from '../utils';

export const getCourses = (): void => {
    apiClient.get('course/', {params: {'view': true}})
        .then((response: AxiosResponse) => {
            setCourses(response?.data);
        })
        .catch(() => {
            message.error('Error with getting courses');
        });
};
export const getCourse = (id: string): void => {
  apiClient.get(`course/${id}/`, {})
    .then((response: AxiosResponse) => {
      setCurrentCourse(response?.data);
    })
    .catch(() => {
      message.error('Error with getting courses');
    });
};
export const getMyCourses = (): void => {
  apiClient.get('course/')
    .then((response: AxiosResponse) => {
      setMyCourses(response?.data);
    })
    .catch(() => {
      message.error('Error with getting courses');
    });
};
export const getLesson = (id: string): void => {
  apiClient.get(`lesson/${id}/`, {})
    .then((response: AxiosResponse) => {
      setCurrentLesson(response?.data);
    })
    .catch(() => {
      message.error('Error with getting courses');
    });
};
export const answer = (id: string): void => {
  apiClient.put(`answer/${id}/`, {})
    .then((response: AxiosResponse) => {
      message.success('Successfully answered');
    })
    .catch(() => {
      message.error('Error with answering');
    });
};
