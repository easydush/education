import { apiClient } from './client';
import { AxiosResponse } from 'axios';
import { message } from 'antd';
import { setCourses, setMyCourses } from '../utils';

export const getCourses = (): void => {
    apiClient.get('course/', {params: {'view': true}})
        .then((response: AxiosResponse) => {
            setCourses(response?.data);
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
