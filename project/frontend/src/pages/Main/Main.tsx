import React, { useCallback, useEffect, useMemo, useState } from 'react';
import { Layout, Table } from 'antd';
import { HeaderCustom } from '../../components/Header';
import { ColumnsType } from 'antd/lib/table';
import { Course } from '../../types/course';
import { InfoBlock, PageHeaderText, StyledContent, StyledPageHeader } from './styles';
import { authorize, getCourses } from "../../api";
import { getCurrentCourses } from "../../utils";
import { Link } from "react-router-dom";
import { subscribe } from "../../api/studying";

export const Main = (): JSX.Element => {
  const [loading, setLoading] = useState<boolean>(false);
  const [data, setData] = useState<Course[]>([]);
  const handleJoin = useCallback((courseId) => {
    subscribe(courseId);
  }, []);
  const columns = useMemo(
    () =>
      [
        {
          title: 'Название',
          dataIndex: 'title',
          width: '20%',
          render: function renderName(value, record) {
            return (
              <p>
                {record.title}
              </p>
            );
          },
          sorter: (a, b) => a.title.localeCompare(b.title),
        },
        {
          title: 'Преподаватель',
          dataIndex: 'teacher',
          render: function renderTeacher(value, record) {
            return (
              <p>
                {record.teacher.name}
              </p>
            );
          },
          sorter: (a, b) => a?.teacher?.name?.localeCompare(b.teacher.name),
        },
        {
          title: '',
          dataIndex: 'join',
          render: function renderJoin(value, record) {
            return (
              <Link to={'course/'+record.id}>
                Подробнее
              </Link>);
          },
        },
      ] as ColumnsType<Course>,
    [],
  );
  useEffect(() => {
    async function getData() {
      setLoading(true);
      await setTimeout(() => {
        getCourses();
        setData(getCurrentCourses() ?? []);
        setLoading(false);
      }, 500);
    }

    getData();
  }, []);
  return (
    <Layout>
      <HeaderCustom />
      <StyledContent>
        <StyledPageHeader title={<PageHeaderText>Курсы</PageHeaderText>} backIcon={false} />
        <InfoBlock>
          <Table<Course>
            columns={columns}
            dataSource={data}
            loading={loading}
            pagination={{ pageSize: 7 }}
          />
        </InfoBlock>
      </StyledContent>
    </Layout>
  );
};
